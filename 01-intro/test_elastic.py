from elasticsearch import Elasticsearch

es_client = Elasticsearch("http://localhost:9200")

print(es_client.info())
