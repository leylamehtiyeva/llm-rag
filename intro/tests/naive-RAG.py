from openai import OpenAI
from faq import context
from config import MODEL_NAME

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

def use_llm(prompt: str):
    response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
        ]
    )
    return response.choices[0].message.content

question = "hey,can i still join the course?"
# answer = use_llm(question)

# print(answer)

keyword = "I just discovered the course"
idx = context.find(keyword)

loaded_context = context[idx:idx + 1000]

prompt = f'''
Your task is to answer questions from the course participants based on the
provided context. 
Use the contex to find relevant information and provide accurate answers. 
If the answer is not found in the context respond with "I don't know".


Question: {question}


Context : {loaded_context}
'''

answer = use_llm(prompt)

print(answer)

