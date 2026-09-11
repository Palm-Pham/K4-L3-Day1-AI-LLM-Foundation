import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

response = client.chat.completions.create(
    model="nvidia/nemotron-3-ultra-550b-a55b:free",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. Give accurate, concise answers."
        },
        {
            "role": "user",
            "content": "Explain the difference between Random Forest and LightGBM."
        }
    ],
    temperature=0.3,
    max_tokens=1000,
)

print(response.choices[0].message.content)