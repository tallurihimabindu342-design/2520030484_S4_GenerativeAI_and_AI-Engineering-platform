
"""Compare model-selection strategies using saved benchmark results."""

import csv
from collections import defaultdict
from statistics import mean

from model_router import (
    LARGE_MODEL,
    MODEL_COST_PER_1K,
    SMALL_MODEL,
    analyze_query,
    select_model,
)

RESULTS_FILE = "benchmark_results.csv"
LEVELS = ["Easy", "Medium", "Complex"]


def load_results():
    runs = defaultdict(list)
    expected = {}

    with open(RESULTS_FILE, newline="", encoding="utf-8-sig") as file:
        for row in csv.DictReader(file):
            runs[(row["question"], row["model"])].append(row)
            expected[row["question"]] = row["expected_complexity"]

    return runs, expected


def summarize(rows, model):
    tokens = mean(int(r["total_tokens"]) for r in rows)

    return {
        "seconds": mean(float(r["response_time"]) for r in rows),
        "tokens": tokens,
        "cost": tokens / 1000 * MODEL_COST_PER_1K[model],
        "truncated": any(
            r["done_reason"] == "length" for r in rows
        ),
    }


def main():
    runs, expected = load_results()

    questions = [
        q for q in expected
        if (q, SMALL_MODEL) in runs and (q, LARGE_MODEL) in runs
    ]

    if not questions:
        print("No question has results for both models yet.")
        return

    stats = {
        q: {
            m: summarize(runs[(q, m)], m)
            for m in (SMALL_MODEL, LARGE_MODEL)
        }
        for q in questions
    }

    configs = {
        "Always 1b": lambda q: SMALL_MODEL,
        "Always 3b": lambda q: LARGE_MODEL,
        "Router": lambda q: select_model(analyze_query(q)),
    }

    print(f"\nQuestions analysed: {len(questions)}\n")

    header = (
        f"{'Configuration':<14}"
        f"{'Avg time (s)':>14}"
        f"{'Avg tokens':>12}"
        f"{'Total cost ($)':>16}"
        f"{'Sent to 3b':>12}"
    )

    print(header)
    print("-" * len(header))

    totals = {}

    for name, choose in configs.items():
        chosen = [(q, choose(q)) for q in questions]
        picked = [stats[q][m] for q, m in chosen]

        totals[name] = {
            "seconds": mean(p["seconds"] for p in picked),
            "cost": sum(p["cost"] for p in picked),
        }

        share = sum(
            m == LARGE_MODEL for _, m in chosen
        ) / len(chosen)

        print(
            f"{name:<14}"
            f"{totals[name]['seconds']:>14.2f}"
            f"{mean(p['tokens'] for p in picked):>12.0f}"
            f"{totals[name]['cost']:>16.5f}"
            f"{share:>11.0%}"
        )

    big = totals["Always 3b"]
    router = totals["Router"]

    print(
        f"\nRouter vs always-3b: "
        f"{(1 - router['cost'] / big['cost']):.1%} cheaper, "
        f"{(1 - router['seconds'] / big['seconds']):.1%} faster"
    )

    confusion = {
        e: {p: 0 for p in LEVELS}
        for e in LEVELS
    }

    for q in questions:
        confusion[expected[q]][analyze_query(q)] += 1

    correct = sum(
        confusion[level][level] for level in LEVELS
    )

    print(
        f"\nRouting accuracy: {correct}/{len(questions)} "
        f"({correct / len(questions):.0%})"
    )

    print(
        f"{'Expected':<10}"
        + "".join(f"{'->' + p:>10}" for p in LEVELS)
    )

    for e in LEVELS:
        print(
            f"{e:<10}"
            + "".join(f"{confusion[e][p]:>10}" for p in LEVELS)
        )

    cut_off = [
        q for q in questions
        if any(
            stats[q][m]["truncated"]
            for m in stats[q]
        )
    ]

    if cut_off:
        print(
            f"\nWarning: {len(cut_off)} question(s) "
            "hit the token limit."
        )

    print(
        "\nNote: Answer quality is not measured yet. "
        "Costs are simulated, not actual Ollama charges."
    )


if __name__ == "__main__":
    main()