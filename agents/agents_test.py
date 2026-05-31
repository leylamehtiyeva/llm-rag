from openai import OpenAI
from common.config import OPENAI_API_KEY, MODEL_NAME
from intro.search import ElasticRetriever
import json



from pathlib import Path
client = OpenAI(
    api_key=OPENAI_API_KEY,
)

from intro.search import ElasticRetriever

retriever = ElasticRetriever()

def search(query: str):
    return retriever.search(query=query)


QUESTION = "I just discovered the course, can i still join it?"
    
#Lets define our search tool

search_tool = {
    "type": "function",
    "name": "search",
    "description": "Search the FAQ database for entries matching the given query.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query text to look up in the course FAQ."
            }
        },
        "required": ["query"],
        "additionalProperties": False
    }
}



messages = [
    {"role": "user", "content": QUESTION},
]

response = client.responses.create(
    model=MODEL_NAME,
    input=messages,
    tools=[search_tool],
)

call = response.output[0]

args = json.loads(call.arguments)
result = search(**args)

result_json = json.dumps(result, indent=2)



function_call_output = {
    "type": "function_call_output",
    'call_id': call.call_id,
    'output': result_json,
}

messages.extend(response.output)
messages.append(function_call_output)

# print(messages)

response = client.responses.create(
    model=MODEL_NAME,
    input=messages,
    tools=[search_tool],
)

# print(response.output_text)
# print(response.usage.input_tokens, response.usage.output_tokens)


# --------------- Step3 Adding Agent loop ------------

instructions = """
You're a course teaching assistant.
You're given a question from a course student and your task is to answer it.

If you want to look up information, use the search function. 
Use as many keywords from the user question as possible when making first requests.

Make multiple searches.

Try to expand your search by using new keywords
based on the results you get from the search.

At the end, ask if there are other areas that the user wants to explore.
""".strip()


def make_call(call):
    args = json.loads(call.arguments)

    if call.name == "search":
        result = search(**args)

    result_json = json.dumps(result, indent=2)

    return {
        "type": "function_call_output",
        "call_id": call.call_id,
        "output": result_json,
    }


def agent_loop(instructions, question, model, max_iterations=5) -> str:
    messages = [
        {"role": "developer", "content": instructions},
        {"role": "user", "content": question}
    ]

    it = 1
    last_answer = None

    while it <= max_iterations:
        print(f"iteration #{it}...")
        has_function_calls = False

        response = client.responses.create(
            model=model,
            input=messages,
            tools=[search_tool]
        )

        messages.extend(response.output)

        for item in response.output:
            if item.type == "function_call":
                print("function_call:", item.name, item.arguments)
                call_output = make_call(item)
                messages.append(call_output)
                has_function_calls = True

            elif item.type == "message":
                print("ASSISTANT:")
                last_answer = item.content[0].text
                print(item.content[0].text)

        it = it + 1
        if has_function_calls == False:
            break

    return last_answer

print(agent_loop(instructions, "How do I run Olama locally?", MODEL_NAME))








