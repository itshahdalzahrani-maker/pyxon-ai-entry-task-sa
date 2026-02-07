import chromadb
from sentence_transformers import SentenceTransformer


class VectorDB:
    def __init__(self, collection_name="documents"):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )
        self.model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

    def add_texts(self, texts: list[str]):
        embeddings = self.model.encode(texts).tolist()
        ids = [f"id_{i}" for i in range(len(texts))]

        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            ids=ids
        )

    def search(self, query: str, k: int = 3):
        query_embedding = self.model.encode([query]).tolist()

        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=k
        )

        return results["documents"][0]