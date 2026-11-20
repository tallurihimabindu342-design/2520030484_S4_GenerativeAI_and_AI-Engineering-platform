"""Run every question through every model and log timing and token data.

Every question goes to BOTH models. The router is evaluated afterwards by
analyze_results.py, which simply looks up the row for the model the router
would have picked. No extra model calls are needed.
"""

import csv
import time

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELS = ["llama3.2:1b", "llama3.2:3b"]
QUESTIONS_FILE = "questions.csv"
OUTPUT_FILE = "benchmark_results.csv"

REPEATS = 1  # raise to 3 for the final run: timings are noisy, answers are not
QUESTION_LIMIT = None  # smoke test: only the first 2 questions. Use None for all 30
PROMPT_PREFIX = "Answer clearly in no more than 80 words.\n\n"
NUM_PREDICT = 400

FIELDS = [
    "question", "expected_complexity", "model", "run",
    "response_time", "load_time", "tokens_per_sec",
    "input_tokens", "output_tokens", "total_tokens",
    "done_reason", "answer",
]


def load_questions():
    with open(QUESTIONS_FILE, newline="", encoding="utf-8-sig") as file:
        return list(csv.DictReader(file))


def generate(model, prompt, num_predict):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
            "keep_alive": "10m",
            "options": {"num_predict": num_predict, "temperature": 0},
        },
        timeout=240,
    )
    response.raise_for_status()
    return response.json()


def main():
    questions = load_questions()
    if QUESTION_LIMIT is not None:
        questions = questions[:QUESTION_LIMIT]
    failures = 0

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()

        # Model is the OUTER loop so each model is loaded once, not swapped
        # in and out between questions.
        for model in MODELS:
            print(f"\n=== {model}: warming up (not recorded) ===")
            try:
                generate(model, "Hi", 1)
            except requests.exceptions.RequestException as error:
                print("Warm-up failed, skipping model:", error)
                continue

            for item in questions:
                question = item["question"]
                for run in range(1, REPEATS + 1):
                    print(f"[{model}] run {run}: {question[:60]}")
                    start = time.perf_counter()
                    try:
                        data = generate(
                            model, PROMPT_PREFIX + question, NUM_PREDICT
                        )
                    except requests.exceptions.RequestException as error:
                        failures += 1
                        print("  Error:", error)
                        continue

                    elapsed = time.perf_counter() - start
                    input_tokens = data.get("prompt_eval_count", 0)
                    output_tokens = data.get("eval_count", 0)
                    eval_seconds = data.get("eval_duration", 0) / 1e9

                    writer.writerow({
                        "question": question,
                        "expected_complexity": item["expected_complexity"],
                        "model": model,
                        "run": run,
                        "response_time": round(elapsed, 2),
                        "load_time": round(
                            data.get("load_duration", 0) / 1e9, 2
                        ),
                        "tokens_per_sec": round(
                            output_tokens / eval_seconds, 1
                        ) if eval_seconds else 0,
                        "input_tokens": input_tokens,
                        "output_tokens": output_tokens,
                        "total_tokens": input_tokens + output_tokens,
                        "done_reason": data.get("done_reason", ""),
                        "answer": data.get("response", ""),
                    })
                    file.flush()  # keep partial results if the run is stopped

    print(f"\nDone. Results saved to {OUTPUT_FILE}. Failed calls: {failures}")


if __name__ == "__main__":
    main()