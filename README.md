# llm-rag# Local RAG Setup (Ollama + Elasticsearch)

## 1. Activate virtual environment

```bash
source .venv/bin/activate
```

## 2. Start Ollama server

Open separate terminal:

```bash
ollama serve
```

## 3. Check available models

```bash
ollama list
```

## 4. Pull model (only once)

```bash
ollama pull llama3.2:1b
```

or:

```bash
ollama pull llama3.2:3b
```

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

## 6. Check Elasticsearch

```bash
curl http://localhost:9200
```

## 7. Download FAQ documents

```bash
python 01-intro/load_documents.py
```

This creates:

```text
01-intro/data/documents.json
```

## 8. Index documents into Elasticsearch

```bash
python 01-intro/index_elastic.py
```

## 9. Test search

```bash
python 01-intro/search.py
```

## 10. Run full RAG pipeline

```bash
python 01-intro/advanced-RAG.py
```

## Current architecture

```text
User Question
↓
Elasticsearch Retrieval
↓
Top-k Relevant Documents
↓
Prompt Construction
↓
Ollama LLM
↓
Final Answer
```