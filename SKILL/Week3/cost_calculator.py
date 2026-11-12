
# cost_calculator.py

# Example rates per 1 million tokens.
# These are sample values, not verified current Gemini prices.

PRICING = {
    "gemini-3.8-flash": {
        "input": 0.50,
        "output": 2.00
    }
}


def calculate_cost(provider, model, input_tokens, output_tokens):
    # Ollama runs locally and does not charge per-token API fees.
    if provider == "OllamaProvider":
        return 0.0

    # Get pricing information for the selected model.
    rates = PRICING.get(model)

    # Return None if pricing is unavailable.
    if rates is None:
        return None

    # Calculate input token cost.
    input_cost = (input_tokens * rates["input"]) / 1_000_000

    # Calculate output token cost.
    output_cost = (output_tokens * rates["output"]) / 1_000_000

    # Calculate total cost.
    total_cost = input_cost + output_cost

    return round(total_cost, 10)