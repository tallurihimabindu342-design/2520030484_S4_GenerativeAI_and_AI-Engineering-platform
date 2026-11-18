
import requests
import time

from model_router import analyze_query, select_model

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_response(question):
    complexity = analyze_query(question)
    model = select_model(complexity)

    print("\n========== QUERY ANALYSIS ==========")
    print("Query complexity:", complexity)
    print("Selected model:", model)

    print("\nConnecting to Ollama...")

    start_time = time.perf_counter()

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": question,
                "stream": False,
                "options": {
                    "num_predict": 250,
                    "temperature": 0.3
                }
            },
            timeout=180
        )

        response.raise_for_status()
        data = response.json()

        elapsed = time.perf_counter() - start_time

        input_tokens = data.get("prompt_eval_count", 0)
        output_tokens = data.get("eval_count", 0)
        generation_seconds = (
            data.get("eval_duration", 0) / 1_000_000_000
        )

        print("\n========== AI RESPONSE ==========")
        print(data["response"])

        print("\n======= PERFORMANCE METRICS =======")
        print("Query complexity:", complexity)
        print("Model selected:", model)
        print("Response time:", round(elapsed, 2), "seconds")
        print("Input tokens:", input_tokens)
        print("Output tokens:", output_tokens)
        print("Total tokens:", input_tokens + output_tokens)

        if generation_seconds > 0:
            print(
                "Generation speed:",
                round(output_tokens / generation_seconds, 2),
                "tokens/second"
            )

    except requests.exceptions.RequestException as error:
        print("Error connecting to Ollama:", error)


if __name__ == "__main__":
    print("AI Model Selection Framework")
    print("----------------------------")

    question = input("Enter your question: ")
    generate_response(question)