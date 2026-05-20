from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

response = client.chat.completions.create(
    model="llama3.2:1b",
    messages=[
        {
            "role": "user",
            "content": "Can I still join the course?"
        }
    ]
)

print(response.choices[0].message.content)
print(response.model_dump_json(indent=2))