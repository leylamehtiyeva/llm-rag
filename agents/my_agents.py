from openai import OpenAI
from common.config import OPENAI_API_KEY, MODEL_NAME
from intro.search import ElasticRetriever
import json
from dataclasses import dataclass

#Step1
openai_client = OpenAI(api_key=OPENAI_API_KEY)

retriever = ElasticRetriever()

def agent_search(query):
    return retriever.search(query=query)

#Step2

search_tool = {
    "type": "function",
    "name": "agent_search",
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

@dataclass
class FunсtionalToolCall:
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

def make_functional_call(functional_call: FunсtionalToolCall) -> dict[str, str]:
    call_args = json.loads(functional_call.arguments)
    
    if functional_call.name == 'agent_search':
        search_result = agent_search(**call_args)
    else:
        raise ValueError(f"Unsupported functional call: {functional_call.name}")
        
    search_result_json = json.dumps(search_result, indent=2)
    
    return {
        "type": "function_call_output",
        "call_id": functional_call.call_id,
        "output": search_result_json,
    }
    
    
def agent_loop(question: str, 
               model_name: str,
               max_iter: int = 5):
    
    messages=[
        {"role": "developer", "content": orchestrator_instructions},
        {"role": "user", "content": question}  
    ]
    
    i = 1
    last_answer = None
    
    while i <= max_iter:
        print(f"Iteration number # {i}")
        has_function_calls = False
        response = openai_client.responses.create(
            model=model_name,
            input=messages,
            tools=[search_tool]
            )
        
        messages.extend(response.output)
        
        for item in response.output:
            if item.type == "function_call":
                call_json = make_functional_call(item)
                messages.append(call_json)
                has_function_calls = True
            
            elif item.type == "message":
                last_answer = item.content[0].text
                
            else:
                raise TypeError(f"There is no type {item.type}")
                
            
        i += 1
        if not has_function_calls:
            break
        
    return last_answer





                
            
        
        
    
    
    
    
