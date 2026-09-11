import os
import time
from openai import OpenAI

MODEL = "nvidia/nemotron-3-ultra-550b-a55b:free"

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError(
        "OPENROUTER_API_KEY is missing. "
        "Export the key before running this program."
    )

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

print(f"Model: {MODEL}")
print("Chatbot is ready. Type 'exit' to stop.\n")

while True:
    prompt = input("You: ").strip()

    if prompt.lower() in {"exit", "quit"}:
        print("Chatbot stopped.")
        break

    if not prompt:
        continue

    start_time = time.perf_counter()
    first_token_time = None

    try:
        stream = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful AI assistant. "
                        "Answer clearly and concisely."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.3,
            max_tokens=1000,
            stream=True,
        )

        print("\nAssistant: ", end="", flush=True)

        for chunk in stream:
            content = chunk.choices[0].delta.content

            if content:
                if first_token_time is None:
                    first_token_time = time.perf_counter()

                print(content, end="", flush=True)

        end_time = time.perf_counter()

        print("\n")

        if first_token_time is not None:
            first_token_latency = first_token_time - start_time
            print(
                f"Time to first token: "
                f"{first_token_latency:.2f} seconds"
            )

        total_latency = end_time - start_time
        print(f"Total response time: {total_latency:.2f} seconds")
        print("-" * 60)

    except Exception as error:
        print(f"\nAPI error: {error}")
        print("-" * 60)