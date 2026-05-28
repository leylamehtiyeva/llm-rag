

def use_llm(instructions: str, user_prompt: str, client, model):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": instructions,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        temperature=0,
        max_tokens=200,
    )

    return response.choices[0].message.content




def build_context(search_result):
    context = ""

    for doc in search_result:
        context += f"Question: {doc['question']}\n"
        context += f"Answer: {doc['answer']}\n\n"

    return context


def build_prompt(question, search_result):
    context = build_context(search_result)

    return f"""
CONTEXT:
{context}

QUESTION:
{question}

"""



INSTRUCTIONS = """
You are a course FAQ assistant.
Use the provided context to answer the user question.
If the context contains a relevant answer, answer it directly.
Say "I don't know" only if none of the context items are relevant.
Return only the final answer.
"""