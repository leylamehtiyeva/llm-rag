from openai import OpenAI
from common.config import OPENAI_API_KEY, OPENAI_MODEL_NAME
# from intro.search import ElasticRetriever
import json
from dataclasses import dataclass
from pprint import pprint

#Step1
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# retriever = ElasticRetriever()


#Объявим наши тулы, которыми может пользоваться агент.
def agent_search(query):
    return query

def get_course_status():
    return {
        "course_name": "LLM Zoomcamp",
        "enrollment_status": "open",
        "can_join_late": True,
        "message": "Students may join after the official start date."
    }
    
    
    
def print_messages(messages) -> None:
    print("\n========== MESSAGES ==========")

    for index, message in enumerate(messages, start=1):
        print(f"\n--- Message #{index} ---")

        if isinstance(message, dict):
            pprint(message)
        else:
            print(message.model_dump_json(indent=2))

    print("\n==============================")

#Step2

search_tool = {
    "type": "function",
    "name": "agent_search",
    "description": (
        "Search the course FAQ for general information, rules, "
        "policies, and answers to student questions."
    ),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": (
                    "A concise search query containing the important "
                    "keywords from the student's question."
                )
            }
        },
        "required": ["query"],
        "additionalProperties": False
    }
}


course_status_tool = {
    "type": "function",
    "name": "get_course_status",
    "description": (
        "Get the current course enrollment status. "
        "Use this when the student asks whether enrollment is currently "
        "open or whether they can still join the course."
    ),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {},
        "required": [],
        "additionalProperties": False
    }
}

@dataclass
class FunctionalToolCall:
    name: str
    call_id: str
    arguments: str
    
    

#Step3 
orchestrator_instructions = """
You're a course teaching assistant.
You're given a question from a course student and your task is to answer it.

If you want to look up information, use the search function. 
Use as many keywords from the user question as possible when making first requests.

Make multiple searches.

Try to expand your search by using new keywords
based on the results you get from the search.

At the end, ask if there are other areas that the user wants to explore.
""".strip()

#Step4

def make_functional_call(
    functional_call: FunctionalToolCall,
) -> dict[str, str]:
    call_args = json.loads(functional_call.arguments)

    if functional_call.name == "search":
        result = agent_search(**call_args)

    elif functional_call.name == "get_course_status":
        result = get_course_status()

    else:
        raise ValueError(
            f"Unsupported functional call: {functional_call.name}"
        )

    return {
        "type": "function_call_output",
        "call_id": functional_call.call_id,
        "output": json.dumps(result, indent=2),
    }
    
    
def agent_loop(
    question: str,
    model_name: str,
    max_iter: int = 5,
):
    messages = [
        {
            "role": "developer",
            "content": orchestrator_instructions,
        },
        {
            "role": "user",
            "content": question,
        },
    ]

    tools = [
        search_tool,
        course_status_tool,
    ]

    i = 1
    last_answer = None

    while i <= max_iter:
        print(f"\n\n{'=' * 20}")
        print(f"ITERATION #{i}")
        print(f"{'=' * 20}")

        has_function_calls = False

        print("\nMESSAGES SENT TO MODEL:")
        print_messages(messages)

        print("\nTOOLS AVAILABLE TO MODEL:")
        pprint(tools)

        response = openai_client.responses.create(
            model=model_name,
            input=messages,
            tools=tools,
        )

        print("\nRAW RESPONSE OUTPUT:")

        for item in response.output:
            print(item.model_dump_json(indent=2))

        messages.extend(response.output)

        for item in response.output:
            if item.type == "function_call":
                print("\nMODEL DECIDED TO CALL A TOOL")
                print("Tool name:", item.name)
                print("Tool arguments:", item.arguments)
                print("Call ID:", item.call_id)

                call_result = make_functional_call(item)

                print("\nPYTHON TOOL RESULT:")
                pprint(call_result)

                messages.append(call_result)
                has_function_calls = True

            elif item.type == "message":
                last_answer = item.content[0].text

                print("\nMODEL PRODUCED FINAL MESSAGE:")
                print(last_answer)

            elif item.type == "reasoning":
                print("\nREASONING ITEM:")

                if item.summary:
                    for summary_part in item.summary:
                        print(summary_part.text)
                else:
                    print("No reasoning summary was returned.")

            else:
                raise TypeError(f"There is no type {item.type}")

        print("\nMESSAGES AFTER ITERATION:")
        print_messages(messages)

        i += 1

        if not has_function_calls:
            break

    return last_answer




if __name__ == "__main__":
    answer = agent_loop(
        question="Can I still join the course?",
        model_name=OPENAI_MODEL_NAME,
    )

    print("\nFinal answer:")
    print(answer)
                
            
        
        
    
    
    
    
