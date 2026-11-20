"""Query analysis and model routing for the GenAI model-selection framework."""

import re

SMALL_MODEL = "llama3.2:1b"
LARGE_MODEL = "llama3.2:3b"

# Simulated price in USD per 1K tokens. Local Ollama models are free, so these
# are assumptions that scale roughly with parameter count (~1.2B vs ~3.2B).
MODEL_COST_PER_1K = {
    SMALL_MODEL: 0.0002,
    LARGE_MODEL: 0.0006,
}

# Which model handles which complexity level. Because analyze_results.py
# replays the benchmark data, you can change this table (e.g. Medium ->
# SMALL_MODEL) and re-run the analysis without re-running the benchmark.
ROUTING_TABLE = {
    "Easy": SMALL_MODEL,
    "Medium": LARGE_MODEL,
    "Complex": LARGE_MODEL,
}

# Task verbs (with common endings) that signal harder work. Matching is on
# whole words, so "optimized" and "comparing" are caught but "developer" and
# "architecture" are not.
COMPLEX_PATTERN = re.compile(
    r"\b(?:(?:design|develop|optimi[sz]|debug|implement|architect|evaluat|"
    r"compar|analy[sz]|prove|deriv)(?:e|es|ed|ing|s)?|analysis|comparison)\b"
)

MEDIUM_PATTERN = re.compile(
    r"\b(?:explain|describe|how|why|differences?|advantages?|"
    r"disadvantages?|summari[sz]e)\b"
)

# Looks for real code shapes (fenced block, "def f(", arrow functions,
# "f(x):" / "f(x) {"), not stray punctuation like ; or { } in normal prose.
CODE_PATTERN = re.compile(r"```|\bdef \w+\(|=>|\w+\([^)]*\)\s*[{:]")


def explain_query(question):
    """Return (complexity, reasons) so the decision can be shown to users."""
    text = question.lower().strip()
    word_count = len(re.findall(r"\b\w+\b", text))
    score = 0
    reasons = []

    if COMPLEX_PATTERN.search(text):
        score += 2
        reasons.append("contains a task verb such as design/compare/analyze")
    if MEDIUM_PATTERN.search(text):
        score += 1
        reasons.append("asks for an explanation")
    if CODE_PATTERN.search(question):
        score += 2
        reasons.append("contains code")
    if word_count > 60:
        score += 2
        reasons.append(f"long query ({word_count} words)")
    elif word_count > 25:
        score += 1
        reasons.append(f"fairly long query ({word_count} words)")
    if question.count("?") > 1:
        score += 1
        reasons.append("contains multiple questions")

    if score >= 2:
        complexity = "Complex"
    elif score == 1:
        complexity = "Medium"
    else:
        complexity = "Easy"

    if not reasons:
        reasons.append("short, direct question")
    return complexity, reasons


def analyze_query(question):
    """Same signature as before, so main.py keeps working."""
    return explain_query(question)[0]


def select_model(complexity):
    return ROUTING_TABLE.get(complexity, LARGE_MODEL)