from openai import OpenAI
from common.config import OPENAI_API_KEY, MODEL_NAME
from intro.search import ElasticRetriever
import json
from dataclasses import dataclass

#Step1
openai_client = OpenAI(api_key=OPENAI_API_KEY)

retriever = ElasticRetriever()


#Объявим наши тулы, которыми может пользоваться агент.
def agent_search(query):
    return retriever.search(query=query)

def get_course_status():
    return {
        "course_name": "LLM Zoomcamp",
        "enrollment_status": "open",
        "can_join_late": True,
        "message": "Students may join after the official start date."
    }

#Step2

search_tool = {
    "type": "function",
    "name": "search",
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

def make_functional_call(functional_call: FunctionalToolCall) -> dict[str, str]:
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
        
        tools = [
            search_tool,
            course_status_tool,
        ]
        response = openai_client.responses.create(
            model=model_name,
            input=messages,
            tools=tools
            )
        
        messages.extend(response.output)
        
        for item in response.output:
            if item.type == "function_call":
                call_json = make_functional_call(item)
                messages.append(call_json)
                has_function_calls = True
                
            elif item.name == "get_course_status":
                result = get_course_status(**arguments)
            
            elif item.type == "message":
                last_answer = item.content[0].text
            
            elif item.type == "reasoning":
                continue
                
            else:
                raise TypeError(f"There is no type {item.type}")
                
            
        i += 1
        if not has_function_calls:
            break
        
    return last_answer





                
            
        
        
    
    
    
    
