# LLM-RAG

Local RAG system built with:

- Ollama
- Elasticsearch
- OpenAI-compatible API
- Python

Current pipeline:

```text
User Question
↓
Elasticsearch Retrieval (BM25)
↓
Top-k Relevant Documents
↓
Context Building
↓
Prompt Construction
↓
Ollama LLM
↓
Final Answer
```

Project structure:

```text
01-intro/
├── data/
│   └── documents.json
├── tests/
├── advanced-RAG.py
├── config.py
├── index_data.py
├── load_documents.py
├── rag_helper.py
├── rag_pipeline.py
└── search.py
```

---

# Setup

## 1. Activate virtual environment

```bash
source .venv/bin/activate
```

---

## 2. Start Ollama server

Open separate terminal:

```bash
ollama serve
```

---

## 3. Check available models

```bash
ollama list
```

---

## 4. Pull model (only once)

```bash
ollama pull llama3.2:1b
```

or:

```bash
ollama pull llama3.2:3b
```

---

## 5. Start Elasticsearch

Open separate terminal:

```bash
docker run -it \
  --rm \
  --name elasticsearch \
  -p 9200:9200 \
  -p 9300:9300 \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  -e "ES_JAVA_OPTS=-Xms512m -Xmx512m" \
  docker.elastic.co/elasticsearch/elasticsearch:8.17.6
```

---

## 6. Check Elasticsearch

```bash
curl http://localhost:9200
```

---

# Data pipeline

## 7. Download FAQ documents

```bash
python 01-intro/load_documents.py
```

Creates:

```text
01-intro/data/documents.json
```

---

## 8. Index documents into Elasticsearch

```bash
python 01-intro/index_data.py
```

---

## 9. Test retrieval

```bash
python 01-intro/search.py
```

---

## 10. Run full RAG pipeline

```bash
python 01-intro/advanced-RAG.py
```

---

# Retrieval

Current retrieval uses:

- Elasticsearch BM25 search
- Multi-field retrieval
- Field boosting
- Metadata filtering

Search fields:

- question
- section
- answer

Metadata filtering:

- course

---

# Current limitations

- No embeddings yet
- No vector search yet
- No reranking
- Small local models may hallucinate or ignore context
- Retrieval currently uses BM25 only
