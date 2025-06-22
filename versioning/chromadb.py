import chromadb
from versioning.rl_search import compute_reward

def search_similar_rl(query: str, n=3):
    results = collection.query(query_texts=[query], n_results=n)
    docs = results["documents"][0]
    
    reranked = sorted(docs, key=lambda doc: compute_reward(query, doc), reverse=True)
    return reranked[:1] 

client = chromadb.PersistentClient(path="db/")
collection = client.get_or_create_collection(name="chapters")

def save_version(chapter_id: str, content: str, metadata: dict):
    collection.add(documents=[content], metadatas=[metadata], ids=[chapter_id])

def search_similar(query: str, n=3):
    res = collection.query(query_texts=[query], n_results=n)
    return res["documents"][0]
