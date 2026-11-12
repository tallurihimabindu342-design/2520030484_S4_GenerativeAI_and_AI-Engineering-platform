import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print("API key loaded:", bool(api_key))
print("API key prefix:", api_key[:3] if api_key else "Missing")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is Artificial Intelligence? Explain in simple words."
)

print("\nLLM Response:")
print(response.text)