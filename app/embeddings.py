from sentence_transformers import SentenceTransformer


class EmbeddingService:
    def _init_(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed(self, texts: list[str]):
        return self.model.encode(texts)