from config import OPENAI_API_KEY, MODEL_NAME
from openai import OpenAI

client = OpenAI(
    api_key=OPENAI_API_KEY,
)

response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {
            "role": "user",
            "content": "hey, can i still join the course?",
        }
    ],
)

print(response.choices[0].message.content)