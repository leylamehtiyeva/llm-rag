from openai import OpenAI
from faq import context
from config import MODEL_NAME
from search import search_from_elastic

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

QUESTION = "hey,can i still join the course?"


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


# To build more advanced RAG system at first we need 3 steps: search, build prompt
# and sending to llm

def build_context(search_result):
    context = ""

    for doc in search_result:
        context += f"Question: {doc['question']}\n"
        context += f"Answer: {doc['answer']}\n\n"

    return context


def build_prompt(question, search_result):
    context = build_context(search_result)

    return f"""
You are a course FAQ assistant.

Answer the user question using only the context below.
If the answer is not in the context, say: I don't know.

Context:
{context}

User question:
{question}

"""


def rag(question):
    search_result = search_from_elastic(query=question, course_type="llm-zoomcamp", top_n=2)
    user_prompt = build_prompt(question, search_result)
    return use_llm(user_prompt)


print(rag(QUESTION))










