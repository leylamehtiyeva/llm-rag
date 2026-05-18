context = r'''
DataTalks.Club FAQ
Home ML Zoomcamp LLM Zoomcamp Data Engineering Zoomcamp MLOps Zoomcamp
LLM Zoomcamp FAQ
💡 Have a question to add? Learn how to contribute to this FAQ!

Table of Contents
General Course-Related Questions
Module 1: Introduction to LLMs and RAG
Module 2: Agents
Module 3: Vector Search
Module 4: Evaluation
Module 5: Monitoring
Module 6: Best Practices
Capstone Project
Workshop: Open-Source Data Ingestion (dlt)
General Course-Related Questions
#I just discovered the course. Can I still join?
Yes, but if you want to receive a certificate, you need to submit your project while we’re still accepting submissions.

edit on GitHub
#Course: I have registered for the LLM Zoomcamp. When can I expect to receive the confirmation email?
You don't need it. You're accepted. You can also just start learning and submitting homework (while the form is open) without registering. It is not checked against any registered list. Registration is just to gauge interest before the start date.

edit on GitHub
#What is the video/zoom link to the stream for the “Office Hours” or live/workshop sessions?
The zoom link is only published to instructors/presenters/TAs.

Students participate via YouTube Live and submit questions to Slido (link is pinned in the chat when live). The video URL should be posted in the announcements channel on Telegram &amp; Slack before it begins. You can also watch live on the DataTalksClub YouTube Channel.

Don’t post questions in chat as they may be missed if the room is very active.

edit on GitHub
#Cloud alternatives with GPU
Check the quota and reset cycle carefully. Is the free hours limit per month or per week? Usually, if you change the configuration, the free hours quota might also be adjusted, or it might be billed separately.

Potential options include:

Google Colab
Kaggle
Databricks (possibly)
Consider using GPTs to discover more options. Be aware that some platforms might have restrictions on what you can and cannot install, so ensure to read what is included in the free vs paid tier.

edit on GitHub
#Leaderboard: I am not on the leaderboard / how do I know which one I am on the leaderboard?
When you set up your account, you are automatically assigned a random name, such as “Lucid Elbakyan.” Click on the "Jump to your record on the leaderboard" link to find your entry.

If you want to see what your Display name is, click on the "Edit Course Profile" button.

image #1

First field: This is your nickname/displayed name. You can change it if you want to be known by your Slack username, GitHub username, or any other nickname of your choice. This is useful if you want to remain anonymous.
Second field: Change this to your official name as in your identification documents—passport, national ID card, driver's license, etc. This is mandatory if you do not want "Lucid Elbakyan" on your certificate. This name will appear on your Certificate!
edit on GitHub
#Certificate: Can I follow the course in a self-paced mode and get a certificate?
No, you can only get a certificate if you finish the course with a "live" cohort.

We don't award certificates for the self-paced mode. The reason is you need to peer-review 3 capstone(s) after submitting your project.

You can only peer-review projects at the time the course is running; after the form is closed and the peer-review list is compiled.

edit on GitHub
#I missed the first homework - can I still get a certificate?
Yes, you need to pass the Capstone project to get the certificate. Homework is not mandatory, though it is recommended for reinforcing concepts, and the points awarded count towards your rank on the leaderboard.

edit on GitHub
#Homework: Why does the content keep changing?
This course is being offered for the first time, and things will keep changing until a given module is ready, at which point it shall be announced. Working on the material or homework in advance will be at your own risk, as the final version could be different.

edit on GitHub
#When will the course be offered next?
Summer 2025.

edit on GitHub
#Are there any lectures/videos? Where are they?
Please check the bookmarks and pinned links, especially DataTalks.Club’s YouTube account.

edit on GitHub
#WSL2: ResponseError: model requires more system memory (X.X GiB) than is available (Y.Y GiB). My system has more than X.X GiB.
Your WSL2 is set to use Y.Y GiB, not all your computer memory. To allocate more RAM, follow these steps:

Create a .wslconfig file under your Windows user profile directory: C:\Users\YourUsername\.wslconfig.

Include the desired RAM allocation in the file:

[wsl2]
memory=8GB
Restart WSL using the command:

wsl --shutdown
Run the free command in WSL to verify the changes.

For more details, read this article.

edit on GitHub
#Server Error (500) When logging in to course homework using GitHub
Additional error text seen:

Third-Party Login Failure

An error occurred while attempting to login via your third-party account.
The current solution is to use Google or Slack to log in and submit homework answers, as the root cause analysis for the GitHub issue is sporadic and doesn’t impact all users.

edit on GitHub
Module 1: Introduction to LLMs and RAG
#Why are we not using Langchain in the course?
Langchain is a framework for building LLM-powered apps. We're not using it to learn the basics; think of it like learning HTML, CSS, and JavaScript before learning React or Angular.

edit on GitHub
#OpenAI: Error when running OpenAI chat.completions.create command
You may receive the following error when running the OpenAI chat.completions.create command due to insufficient credits in your OpenAI account:

OpenAI API Error: Insufficient credits
edit on GitHub
#OpenAI: Error: RateLimitError: Error code: 429 -
RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: [https://platform.openai.com/docs/guides/error-codes/api-errors.](https://platform.openai.com/docs/guides/error-codes/api-errors.)', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}
The above errors are related to your OpenAI API account’s quota. There is no free usage of OpenAI’s API, so you will need to add funds using a credit card (see pay-as-you-go in the OpenAI settings at platform.openai.com). Once added, re-run your Python command and you should receive a successful return code.

Steps to resolve:

Add credits to your account here (min $5).

In chat.completions.create(model='gpt-4o', …) specify one of the models available to you:

image #1

You might need to recreate an API key after adding credits to your account and update it locally.

edit on GitHub
#OpenAI: Error: 'Cannot import name OpenAI from openai'; How to fix?
Update openai version from 0.27.0 to any 1.x version.

edit on GitHub
#OpenAI: How much will I have to spend to use the Open AI API?
Using the OpenAI API does not cost much. You can recharge starting from $5. For initial usage, it might cost as little as 5 cents.

edit on GitHub
#OpenAI: Do I have to subscribe and pay for Open AI API for this course?
No, you don't have to pay for this service in order to complete the course homeworks. You could use some of the free alternatives listed in the course GitHub.

llm-zoomcamp/01-intro/open-ai-alternatives.md at main · DataTalksClub/llm-zoomcamp (github.com)

edit on GitHub
#Authentication: Safe and easy way to store and load API keys
You can store your different API keys in a YAML file that you will add to your .gitignore file. Be careful to never push or share this file.

For example, create a new file named api_keys.yml in your repository.

Then, add it to your .gitignore file:

#api_keys

api_keys.yml
Fill your api_keys.yml file:

OPENAI_API_KEY: "sk[...]"
GROQ_API_KEY: "gqk_[...]"
Save your file.

You will need the pyyaml library to load your YAML file, so run this command in your terminal:

pip install pyyaml
Now, open your Jupyter notebook.

You can load your YAML file and the associated keys with this code:

import yaml

# Open the file
with open('api_keys.yml', 'r') as file:
    # Load the data from the file
    data = yaml.safe_load(file)

# Get the API key (Groq example here)
groq_api_key = data['GROQ_API_KEY']
Now, you can easily replace the api_key value directly with the loaded values without loading your environment variables.

edit on GitHub
#How to store and load API keys using .env file
Store the API key in a .env file, then use the following steps to load it:

Import the necessary modules:

import os
from dotenv import load_dotenv
Load the .env file:

load_dotenv(os.path.abspath("<path-to-.env>"))
Retrieve the API key:

os.getenv("API_KEY_abc")
Ensure to add the .env file to your .gitignore to prevent it from being checked into version control.
edit on GitHub
#Authentication: Why is my OPENAI_API_KEY not found in the Jupyter notebook?
There are two options to resolve this issue:

Option 1: Using direnv

Create a .envrc file and add your API key.
Run direnv allow in the terminal.
If you encounter the error:

OpenAIError: The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable
Install dotenv by running:

pip install python-dotenv
Add the following to a cell in the notebook:

from dotenv import load_dotenv

load_dotenv('.envrc')
Option 2: Using Codespaces Secrets

Log in to your GitHub account and navigate to Settings > Codespaces.
In the Secrets section, create a secret like OPENAI_API_KEY and select the repositories for which the secret should be available.
Once set up, the key will be available in your Codespaces session.
edit on GitHub
#OpenSource: I am using Groq, and it doesn't provide a tokenizer library based on my research. How can we estimate the number of OpenAI tokens asked in homework question 6?
The question asks for the number of tokens in the GPT-4o model. tiktoken is a Python library that can be used to get the number of tokens. You don't need an OpenAI API key to get the number of tokens. You can use the code provided in the question to get the number of tokens.

edit on GitHub
#OpenSource: Can I use Groq instead of OpenAI?
You can use any LLM platform for your experiments and your project. The homework is designed so that you don’t need access to any paid services and can complete it locally. However, you will need to adjust the code for that platform. Refer to their documentation pages.

edit on GitHub
#OpenSource: Can I use open-source alternatives to OpenAI API?
Yes. See module 2 and the open-ai-alternatives.md in the module 1 folder.

edit on GitHub
#OpenAI: "RateLimitError 429 / insufficient_quota" — my account has no credit
RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota...',
'type': 'insufficient_quota'}}
Despite the name, insufficient_quota is not a temporary rate-limit you can wait out — it means your OpenAI account has no paid credit. Two options:

Add a small amount (~$5–$10) on https://platform.openai.com and use a cheap model like gpt-4o-mini.
Switch to a free alternative:
Groq — free tier, OpenAI-compatible API, supports tool use.
Google Gemini — free tier, e.g. gemini-2.0-flash.
Ollama — runs locally, fully free.
The course's curated list of OpenAI-compatible providers: https://github.com/DataTalksClub/llm-zoomcamp/blob/main/awesome-llms.md#openai-api-alternatives

edit on GitHub
#Homework: Returning Empty list after filtering my query (HW Q3)
This is likely to be an error when indexing the data. First, you need to add the index settings before adding the data to the indices, then you will be good to go applying your filters and query.

edit on GitHub
#minsearch: SyntaxError "invalid character" when running my downloaded copy
SyntaxError: invalid character '·' (U+00B7)
You probably saved the GitHub HTML page instead of the raw Python file. Either:

Use the "Raw" button on GitHub, or download from the raw.githubusercontent.com URL.
Or just install from PyPI — it's the recommended path:
pip install -U minsearch
# or
uv add minsearch
edit on GitHub
#ModuleNotFoundError on import docx in parse-faq.ipynb
The correct package name for docx is python-docx, not docx. Make sure to install the package using:

pip install python-docx
edit on GitHub
#How do I count tokens for a non-OpenAI model (Gemini, Mistral, HuggingFace)?
tiktoken only ships tokenizers for OpenAI models. Using cl100k_base for other providers gives wrong counts and unreliable cost estimates.

For other providers, use their native tokenizer:

Gemini:
import google.generativeai as genai
model = genai.GenerativeModel('gemini-2.0-flash')
print(model.count_tokens(prompt))
Hugging Face / open-source models:
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B")
print(len(tok.encode(prompt)))
Mistral: use the official mistral-common tokenizer package.
Don't use cl100k_base as a generic fallback — token counts will diverge from what the provider actually bills.

edit on GitHub
#OpenAI: Why does my token count differ from what OpenAI reports?
When using tiktoken.encode() to count tokens in your prompt, you might see a difference compared to OpenAI’s API response. For instance, you might get 320 tokens, while OpenAI reports 327. This is due to internal tokens added by OpenAI’s chat formatting.

Here’s what happens:

Each message in a chat.completions.create() call (e.g., {role: "user", content: "..."}) adds 4 structural tokens (role, content, separators).
The API adds 2 tokens globally to mark the start of assistant response generation.
Extra newlines, whitespace, or uncommon Unicode characters in your content may slightly increase the token count.
Thus, even if your visible text is 320 tokens, OpenAI may count 327 due to these internal additions.

edit on GitHub
#API keys: how do I set them once and not re-export every terminal?
Use direnv to scope env vars to a project directory. It loads them automatically when you cd in:

# install direnv (Linux: apt/brew; macOS: brew install direnv)
# add this line to your ~/.bashrc or ~/.zshrc:
eval "$(direnv hook bash)"   # or zsh

# inside your project:
echo 'export OPENAI_API_KEY=sk-...' > .envrc
echo '.envrc' >> .gitignore
direnv allow
Important: always add .envrc (and .env) to .gitignore so the key never lands on GitHub.

For GitHub Codespaces, use the built-in Codespaces secrets instead of files in the repo.

For Python scripts, the equivalent is python-dotenv:

from dotenv import load_dotenv
load_dotenv()  # loads .env from project root
edit on GitHub
#Ollama: How to install Ollama?
First, install Ollama by visiting https://ollama.com/download and choosing your operating system:

macOS: Download the .pkg and install it.

Windows: Download the .msi and install it.

Linux: Run the following command in the terminal:

curl -fsSL https://ollama.com/install.sh | sh
Once installed, open a terminal and type:

ollama run llama3
This command will:

Download the LLaMA 3 model (~4GB).
Start the model locally.
Open a chat-like interface where you can type questions.
To test the Ollama local server, run the following command:

curl http://localhost:11434
You should receive a response similar to:

{"models": [...]}  
Then, install the Python client with:

pip install ollama
Here is a minimal Python example:

import ollama

response = ollama.chat(
    model='llama3',
    messages=[{"role": "user", "content": your_prompt}]
)

print(response['message']['content'])
edit on GitHub
Module 2: Agents
#Connection refused error on prompting the ollam RAG?
If you encounter this error while doing the homework, you can resolve it by restarting the Ollama server using the following command:

!nohup ollama serve > nohup.out 2>&1 &
Make sure to rerun the cell containing ollama serve if you stop and restart the notebook cell.

edit on GitHub
#Any free models with tool use support?
Several Groq models offer tool use, such as Deepseek R1 or Llama 4, all of which can be used for free for development.

For more details, please visit: Groq Tool Use Documentation

edit on GitHub
#Agents: "RuntimeError: Already running asyncio in this thread" when calling asyncio.run() from Jupyter
Jupyter already runs an event loop inside the kernel, so calling asyncio.run(...) blows up with:

RuntimeError: Already running asyncio in this thread
In a notebook cell, just await the coroutine directly — no wrapper needed:

result = await main()
For the FastMCP server in the agents homework, use the async variant:

await mcp.run_async()
Note: in the agents homework's "run the server" question, you're meant to start the MCP server from a terminal (python weather_server.py), not from inside the notebook.

edit on GitHub
#I passed a float to my tool, but got a validation error saying it expected a number. Isn’t float a number?
Yes — in Python, float is a numeric type. But when working with FastMCP, tool inputs are validated against JSON Schema, which uses the term "number" to represent any numeric value (integers or floats).

The important thing is not the type you use in Python, but whether the JSON you send matches the tool's declared input schema.

Example:

"inputSchema": {
  "type": "object",
  "properties": {
    "temp": {
      "type": "number"
    }
  },
  "required": ["temp"]
}
Make sure the values in "arguments" match the types declared in the tool’s schema — not Python types, but JSON types (string, number, boolean, etc.).

edit on GitHub
#Agents: which non-OpenAI models support tool / function calling?
Confirmed working alternatives for tool calling in this course:

Groq — llama-3.3-70b-versatile, DeepSeek R1, Llama 4. Free tier, OpenAI-compatible API.
Mistral — most models. Schema differs slightly from OpenAI.
Google Gemini — gemini-2.5-flash etc., free tier. Available either through Google's GenAI SDK or via the OpenAI-compatible endpoint.
Ollama — llama3.1 and similar, local. Use ollama.chat(..., tools=[...]).
You'll typically need to adapt the homework's chat_assistant.py / mcp_client.py slightly when not using OpenAI — the tool schema and the response shape differ between providers.

edit on GitHub
#Install MCP Inspector
Ensure Node.js is installed.

To install the MCP Inspector, run the following command in your terminal:

npm i @modelcontextprotocol/inspector
edit on GitHub
#Agents: "AttributeError: 'str' object has no attribute 'output'" when using OpenAI's Responses API on a non-OpenAI model
The new OpenAI Responses API (client.responses.create(...), accessed via response.output) is OpenAI-specific. Other providers (Mistral, Groq, Gemini, etc.) don't implement it.

For non-OpenAI providers, use the chat-completions API and read response.choices[0].message.content:

response = client.chat.completions.create(
    model="<provider-model>",
    messages=[{"role": "user", "content": prompt}],
    tools=tools_schema,  # may need adapting per provider
)
return response.choices[0].message.content
You'll also have to adapt the tools schema to whatever shape your provider expects.

edit on GitHub
#Run MCP Inspector
To run the MCP Inspector, execute the following command in the terminal:

npx @modelcontextprotocol/inspector
edit on GitHub
#Inspect MCP Server
Connect to the MCP Server

image #1

The inspector can list tools, templates, resources, and prompts from the MCP Server

image #2

Reference:

https://medium.com/@anil.goyal0057/how-to-test-your-mcp-server-using-mcp-inspector-c873c417eec1

edit on GitHub
#How to Solve "RuntimeError: Already running asyncio in this thread"
Jupyter notebooks already run an event loop in the main thread to handle asynchronous code. For this reason, when you try to call asyncio.run() inside a cell, you get the following error:

RuntimeError: asyncio.run() cannot be called from a running event loop
Instead of using asyncio.run(), simply use await directly in the notebook cell.

Incorrect:

import asyncio

async def main():
    async with Client(weather_server.mcp) as mcp_client:
        # your code here

# This will cause the RuntimeError
result = asyncio.run(main())
Correct:

async def main():
    async with Client(weather_server.mcp) as mcp_client:
        # your code here

# Use await directly
result = await main()
Jupyter notebooks automatically create an asyncio event loop when they start. Since asyncio.run() attempts to create a new event loop, it conflicts with the existing loop. By using await directly, you leverage the already running event loop.

edit on GitHub
#I am using Azure OpenAI and I am still getting an error of Error code: 400 - {'error': {'message': "Missing required parameter: 'tools[0].function'.", 'type': 'invalid_request_error', 'param': 'tools[0].function', 'code': 'missing_required_parameter'}}?
Modify the get_weather_tool JSON to be the following:

get_weather_tool = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a specific city or generate fake data",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The name of the city to get the weather for."
                }
            },
            "required": ["city"],
            "additionalProperties": false
        }
    }
}
edit on GitHub
Module 3: Vector Search
#What are embeddings?
Embeddings refer to the process of converting non-numerical data into numerical data while preserving meaning and context. When similar non-numerical data is input into an embedding algorithm, it should yield similar numerical data. The proximity of these numerical values allows for the use of mathematical semantic similarity algorithms. Related concepts include the "vector space model" and "dimensionality reduction."

edit on GitHub
#Warning: 'model "multi-qa-mpnet-base-dot-v1" was made on sentence transformers v3.0.0 bet' how to suppress?
To suppress the warning, upgrade sentence-transformers to version 3.0.0 or higher. You can do this by running the following command:

pip install sentence-transformers>=3.0.0
edit on GitHub
#Why was .dot(...) used directly to compute cosine similarity in the lesson, but normalization is emphasized in the homework?
In the lesson, .dot(...) was used under the assumption that the embeddings returned by the model (e.g., model.encode(...) from OpenAI) are already normalized to have unit length. In that case, the dot product is mathematically equivalent to cosine similarity.

In the homework, however, we use classic embeddings like TF-IDF + SVD, which are not normalized by default. This means that the dot product does not represent cosine similarity unless we manually normalize the vectors.

edit on GitHub
#Vector search: should I embed the question, the answer, or both?
There's no single right answer — it's an experiment to run on your dataset. The course shows three options:

Embed the answer (text) only — works because the model captures semantic similarity between questions and their answers.
Embed the question only — works because user queries look like the indexed questions.
Embed question + " " + text — often the best, but produces longer input and slightly more cost.
Pick whichever gives the best hit rate / MRR on your ground-truth set. The course materials include a side-by-side comparison.

edit on GitHub
#What is the cosine similarity?
Cosine similarity is a measure used to calculate the similarity between two non-zero vectors, often used in text analysis to determine how similar two documents are based on their content. This metric computes the cosine of the angle between two vectors, which are typically word counts or TF-IDF values of the documents. The cosine similarity value ranges from -1 to 1, where 1 indicates that the vectors are identical, 0 indicates that the vectors are orthogonal (no similarity), and -1 represents completely opposite vectors.

edit on GitHub
#Why does cosine similarity reduce to a matrix multiplication between the embeddings and the query vector?
Cosine similarity measures how aligned two vectors are, regardless of their magnitude. When all vectors (including the query) are normalized to unit length, their magnitudes no longer matter. In this case, cosine similarity is equivalent to simply taking the dot product between the query and each document embedding. This allows us to compute similarities efficiently using matrix multiplication.

edit on GitHub
Module 4: Evaluation
#Evaluation: "JSONDecodeError: Expecting value" when generating ground-truth questions with the LLM
The LLM sometimes wraps the JSON in a markdown code fence or adds prose around it, so json.loads(response) fails with:

JSONDecodeError: Expecting value: line 1 column 1 (char 0)
Force JSON output with OpenAI's response_format:

response = openai_client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[{"role": "user", "content": prompt}],
    response_format={"type": "json_object"},
)
parsed = json.loads(response.choices[0].message.content)
Also be explicit in the prompt about the expected shape:

Output a JSON object with a single key "questions" whose value is a list of 5 strings.
Do not include any extra text, explanation, or formatting.
Most providers have an equivalent (Gemini's response_mime_type="application/json", Groq's response_format, etc.).

edit on GitHub
#Evaluation: Jupyter kernel crashes when embedding the ground-truth set
Small-RAM machines (Codespaces default, low-end laptops) run out of memory when an embedding model is loaded alongside the rest of the notebook state.

Workarounds:

Switch to a smaller embedder. sentence-transformers/all-MiniLM-L6-v2 (384-dim) is a common drop-in. Note: switching models will change your hit-rate / MRR numbers, so re-run the eval after the switch.
Move the embedding step into a separate Python script that you run from the terminal, then load the saved vectors back into the notebook.
Use a Codespaces machine type with more RAM (Settings → "Machine type" on a Codespace), or run locally.
Process the ground-truth set in batches and free memory between batches (del, gc.collect()).
edit on GitHub
#Evaluation: hitting rate limits while generating the ground-truth dataset
Free-tier Gemini limits both per-minute and per-day requests. Adding time.sleep(4) only fixes the per-minute side — a long tqdm loop can still blow through the per-day quota in one run.

Options when this happens:

Spend ~$5 on OpenAI and use gpt-4o-mini. It's cheap enough to embed/generate the entire ground-truth set and has higher rate limits.
Use Groq's free tier (llama-3.3-70b-versatile) — generous request-per-minute limits.
Lower concurrency for thread-pool calls. Use a smaller pool size (2–3 workers) instead of pushing the API hard.
Resume from where you stopped. Save progress periodically (e.g. dump the partial results to a JSONL file) so a hit limit doesn't lose all work.
edit on GitHub
Module 5: Monitoring
#In Windows OS: OSError: [WinError 126] The specified module could not be found. Error loading "C:\Users\USER\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\lib\fbgemm.dll" or one of its dependencies.
Solution 1: Install Visual C++ Redistributable.

Solution 2: Install Visual Studio, not Visual Studio Code.

image #1

For more details, please follow this link: discuss.pytorch.org

edit on GitHub
#OperationalError when running python prep.py: psycopg2. OperationalError: could not translate host name "postgres" to address: No such host is known. How do I fix this issue?
To resolve this error, update the .env file:

Change the POSTGRES_HOST variable to localhost.
POSTGRES_HOST=localhost
edit on GitHub
#How set Pandas to show entire text content in a column. Useful to view the entire Explanation column content in the LLM-as-judge section of the offline-rag-evaluation notebook
By default, Pandas truncates text content in a column to 50 characters. To view the entire explanation provided by the judge LLM for a non-relevant answer, use the following instruction:

pd.set_option('display.max_colwidth', None)
Option: display.max_colwidth
Type: int or None
Description: Sets the maximum width in characters of a column in the representation of a pandas data structure. When a column overflows, a "..." placeholder is used in the output. Setting it to 'None' allows unlimited width.
Default: 50
Refer to the official documentation for more details.

image #1

edit on GitHub
#How to normalize vectors in a Pandas DataFrame column (or Pandas Series)?
To normalize vectors in a Pandas DataFrame column, you can use the following approach:

import numpy as np

normalize_vec = lambda v: v / np.linalg.norm(v)

df["new_col"] = df["org_col"].apply(normalize_vec)
edit on GitHub
#How to compute the quantile or percentile of Pandas DataFrame column (or Pandas Series)?
To compute the 75% percentile or 0.75 quantile:

quantile = df["col"].quantile(q=0.75)
edit on GitHub
#How can I remove all Docker containers, images, and volumes, and builds from the terminal?
Delete all containers (including running ones):
docker rm -f $(docker ps -aq)
Remove all images:
docker rmi -f $(docker images -q)
Delete all volumes:
docker volume rm $(docker volume ls -q)
edit on GitHub
#Session State: I want the user to only be able to give feedback once per submission (+1 or -1). When I submit text using the ask button, the buttons should be disabled if `st.session.submitted` is False. The issue is mainly with `st.session.submitted`, which gets reassigned to True again despite one feedback button being pressed.
Solved:

Refer to the solution on Streamlit Discuss

edit on GitHub
Module 6: Best Practices
#Docker: When trying to run a streamlit app using docker-compose, I get: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: "streamlit": executable file not found in $PATH: unknown. The app runs fine outside of docker-compose
To resolve this issue:

Ensure you have created a Dockerfile.

Add streamlit to the docker-compose configuration.

Run the following command to rebuild and start the application:

docker-compose up --build
edit on GitHub
Capstone Project
#Is it a group project?
No, the capstone is a solo project.

edit on GitHub
#Do we submit 2 projects, what does attempt 1 and 2 mean?
You only need to submit one project. If the submission at the first attempt fails, you can improve it and re-submit during the attempt#2 submission window.

If you want to submit two projects for the experience and exposure, you must use different datasets and problem statements.
If you can’t make it to the attempt#1 submission window, you still have time to catch up to meet the attempt#2 submission window.
Remember that the submission does not count towards the certification if you do not participate in the peer-review of three peers in your cohort.

edit on GitHub
#Does the competition count as the capstone?
No, it does not. You can participate in the math-kaggle-llm-competition as a group if you want to form teams; but the capstone is an individual attempt.

edit on GitHub
#How is my capstone project going to be evaluated?
Each submitted project will be evaluated by three randomly assigned students who have also submitted the project.

You will also be responsible for grading the projects from three fellow students yourself. Please be aware that not complying with this rule implies you may fail to achieve the Certificate at the end of the course.

The final grade you receive will be the median score of the grades from the peer reviewers. The peer review criteria for evaluation must follow the guidelines defined here (TBA for link).

edit on GitHub
#When and how will we be assigned projects for review/grading?
After the submission deadline has passed, an Excel sheet will be shared with 3 projects being assigned to each participant.

edit on GitHub
#I’ve already submitted my project. Why can’t I review any projects?
Once the project submission deadline has passed, projects will be assigned to you for evaluation. You can't choose which projects to evaluate, and you can’t review before the list has been released.

edit on GitHub
#How can I find some good ideas or datasets for the project?
Please check this GitHub page for several ideas and datasets that could be used for the project, along with tips and guidelines.

edit on GitHub
#Project: do I need an orchestration tool (Airflow, Mage, Kestra) for the capstone?
No. A plain Python script that ingests and indexes your data is enough for full points on the "ingestion pipeline" criterion. A Jupyter notebook with the same steps is worth 1 point instead of 2.

Use an orchestrator only if it actually fits your project — for example, recurring ingestion of a feed that updates daily. Don't add one just to score the criterion.

edit on GitHub
#Project: how do I evaluate a recommender-style RAG (no obvious Q&A ground truth)?
Two complementary approaches that both score for the evaluation criterion:

Synthetic ground truth (same idea as the course, adapted). For each item in your dataset, prompt the LLM with the item's description and ask it to generate ~5 user queries that should return that item as the top result. Then run those queries through your retrieval and measure hit rate / MRR / NDCG.

LLM-as-a-judge for end-to-end quality. Sample queries, run the full RAG, and have an LLM rate the result for relevance/usefulness on a fixed rubric (e.g. 1–5 scale, with criteria you specify in the prompt).

NDCG is often a better fit than hit-rate for ranking-style problems where multiple items are acceptable answers — it rewards getting good items high in the list, not just first.

edit on GitHub
#Project: my corpus is large (long PDFs, many paragraphs). What's a good chunking strategy?
Don't try to find the perfect chunker upfront — iterate.

Start simple: fixed-size chunking (~1000 tokens with some overlap) and run a small ground-truth eval.
Try smart chunking: ask an LLM to split each document into logical sections, then index each section.
Add a short LLM-generated summary per chunk and index it alongside, or use it to boost retrieval.
For long, structured documents (legal, financial), prefer hybrid search (BM25 + dense) so exact wording isn't lost during semantic matching.
Useful tools for parsing PDFs to clean markdown before chunking:

pymupdf4llm — fast, decent quality.
Docling — slower but higher quality on tables/figures.
GROBID — for academic papers, extracts structure (sections, refs, etc.).
Run the eval again after each change. The goal is measurable improvement on hit rate / MRR for your ground-truth set, not a "perfect" chunker in the abstract.

edit on GitHub
#Project: what does "reproducibility" mean — do reviewers need access to my API keys?
Never share API keys or hosted-service credentials in your repo. Reproducibility means a peer reviewer can clone the repo and follow your README to recreate the system from scratch — using their own credentials.

Concretely:

Provide a script (or notebook) that ingests the dataset and (re)builds the search index locally.
Ship a .env.example with the variable names but no values; have the reviewer create their own .env with their own keys. Keep .env in .gitignore.
Use a cheap model (gpt-4o-mini, Groq, etc.) so reviewers don't burn through credits when running your project.
Pin dependency versions (requirements.txt / pyproject.toml lock file) and document the Python version (and Docker version, if used).
edit on GitHub
Workshop: Open-Source Data Ingestion (dlt)
#Can I use the workshop materials for my own projects or share them with others?
Since dlt is open-source, you can use the content of this workshop for a capstone project. As the main goal of dlt is to load and store data easily, you can even use it for other Zoomcamps (like the MLOps Zoomcamp project). Feel free to ask questions or use it directly in your projects.

edit on GitHub
#How to set up a new dlt project when loading from cloud?
Start with the following command on the command line:

 dlt init filesystem duckdb
More directions can be found at dlthub.com

edit on GitHub
#There is an error when opening the table using `dbtable = db.open_table("notion_pages___homework")`: `FileNotFoundError: Table notion_pages___homework does not exist. Please first call db.create_table(notion_pages___homework, data)`
The error indicates that you have not changed all instances of "employee_handbook" to "homework" in your pipeline settings.

edit on GitHub
#There is an error when running main(): FileNotFoundError: Table notion_pages___homework does not exist. Please first call db.create_table(notion_pages___homework, data)
Make sure you open the correct table in line 3:

dbtable = db.open_table("notion_pages___homework")
edit on GitHub
#How do I know which tables are in the db?
You can use the db.table_names() method to list all the tables in the database.

edit on GitHub
#Does DLT have connectors to ClickHouse or StarRocks?
Currently, DLT does not have connectors for ClickHouse or StarRocks but is open to contributions from the community to add these connectors.

edit on GitHub
#Notebook does not have secret access or 401 Client Error: Unauthorized for url: [api.notion.com](https://api.notion.com/v1/search)
If you encounter this error, it typically indicates an authorization issue with the Notion API. Here’s how you can resolve it:

Check API Key: Ensure that you are using the correct API key with appropriate permissions.
Verify API Endpoint: Confirm that you are hitting the correct Notion API endpoint.
Token Expiry: Check if your token has expired and regenerate it if necessary.
Configurations: Double-check all access configurations in your application.
If the error persists, review the API documentation and make sure all necessary authentication steps are correctly implemented.

edit on GitHub
#Error: How to fix requests library only installs v2.28 instead of v2.32 required for lancedb?
If you encounter a 401 Client Error, it may indicate the need to grant access to the key or that the key is incorrect.

To install the correct version directly from the source, use the following command:

pip install "requests @ https://github.com/psf/requests/archive/refs/tags/v2.32.3.zip"
image #1

edit on GitHub
Generated on 2026-05-12 13:00:57 | DataTalks.Club FAQ
'''
