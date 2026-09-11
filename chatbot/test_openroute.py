import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {"role": "user", "content": "Explain overfitting in machine learning in simple terms."}
    ],
)

print(response.choices[0].message.content)