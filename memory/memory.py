import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection(name="ascendence_memory")

def store(text):
    collection.add(
        documents=[text],
        ids=[str(hash(text))]
    )

def retrieve(query):
    results = collection.query(
        query_texts=[query],
        n_results=3
    )
    return results["documents"][0] if results["documents"] else []