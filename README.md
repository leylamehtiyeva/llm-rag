# LLM-RAG

A Retrieval-Augmented Generation (RAG) system built with Elasticsearch and OpenAI.

The project combines document retrieval, search, and tool-calling workflows to generate grounded answers from an external knowledge base. It demonstrates a production-oriented approach to integrating Large Language Models with search infrastructure.

## Features

* Elasticsearch-based document retrieval
* OpenAI-powered answer generation
* Function Calling support
* Modular retriever architecture
* Dockerized Elasticsearch deployment
* Persistent Elasticsearch storage using Docker volumes
* Extensible tool-calling framework
* Optional support for local models via Ollama

---

## Architecture

```text
User Query
    │
    ▼
Retriever (Elasticsearch)
    │
    ▼
Top-K Relevant Documents
    │
    ▼
Context Construction
    │
    ▼
OpenAI Model
    │
    ▼
Grounded Response
```

---

## Tech Stack

* Python
* OpenAI API
* Elasticsearch
* Docker
* Function Calling
* Jupyter Notebook

---

## Repository Structure

```text
.
├── agents/                 # Function-calling agents
├── intro/                  # Retrieval and indexing logic
├── data/                   # Knowledge base files
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/leylamehtiyeva/llm-rag.git

cd llm-rag
```

### Create a virtual environment

```bash
python -m venv .venv

source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
MODEL_NAME=gpt-4.1-mini
```

---

## Running Elasticsearch

Start Elasticsearch:

```bash
docker start elasticsearch
```

The project uses Docker volumes to persist Elasticsearch data between container restarts.

Verify that Elasticsearch is running:

```bash
curl http://localhost:9200
```

---

## Indexing Documents

Load documents into Elasticsearch:

```bash
python -m intro.index_data
```

This step creates the search index and makes the documents available for retrieval.

---

## Running Search

Example usage:

```python
from intro.search import ElasticRetriever

retriever = ElasticRetriever()

results = retriever.search(
    query="Can I still join the course?"
)

for doc in results:
    print(doc["question"])
```

---

## Running the Agent

Run the function-calling agent:

```bash
python -m agents.agents_test
```

The agent can:

* retrieve relevant documents
* call search tools
* augment prompts with retrieved context
* generate grounded answers using OpenAI models

---

## Example Workflow

1. User submits a question
2. The retriever searches Elasticsearch
3. Relevant documents are returned
4. Context is injected into the prompt
5. The LLM generates a grounded response

---

## Local Models (Optional)

The default setup uses OpenAI models.

To experiment with local inference, install Ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Run a local model:

```bash
ollama run llama3.2
```

The project architecture allows replacing the OpenAI client with a local model endpoint when needed.

---

## Future Improvements

* Hybrid retrieval
* Semantic search with embeddings
* Reranking pipelines
* Evaluation framework
* Multi-tool agents
* Conversational memory
* Advanced RAG workflows

---

## References

* LLM Zoomcamp
* OpenAI API Documentation
* Elasticsearch Documentation
* Ollama Documentation
