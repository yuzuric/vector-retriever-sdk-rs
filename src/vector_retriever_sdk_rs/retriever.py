"""Vector retriever + answer synthesizer using MiMo."""
import asyncio
from pathlib import Path
from dataclasses import dataclass
import numpy as np


@dataclass
class Chunk:
    doc_id: str
    text: str
    score: float = 0.0


class VectorRetriever:
    def __init__(self, index_path: str, embedding_model: str):
        self.index_path = Path(index_path)
        self.embedding_model = embedding_model
        self._embeddings: dict[str, np.ndarray] = {}
        self._texts: dict[str, str] = {}

    async def index(self, documents: list[Path]) -> None:
        for doc in documents:
            text = doc.read_text()
            self._texts[doc.name] = text
            self._embeddings[doc.name] = await self._embed(text)

    async def search(self, query: str, top_k: int = 5) -> list[Chunk]:
        query_vec = await self._embed(query)
        scores = []
        for doc_id, emb in self._embeddings.items():
            score = float(np.dot(query_vec, emb) / (np.linalg.norm(query_vec) * np.linalg.norm(emb)))
            scores.append(Chunk(doc_id=doc_id, text=self._texts[doc_id][:500], score=score))
        return sorted(scores, key=lambda c: c.score, reverse=True)[:top_k]

    async def _embed(self, text: str) -> np.ndarray:
        # Placeholder: real impl would call embedding API
        await asyncio.sleep(0)
        return np.random.rand(384).astype(np.float32)


class AnswerSynthesizer:
    def __init__(self, model: str, api_key: str):
        self.model = model
        self.api_key = api_key

    async def generate(self, query: str, chunks: list[Chunk]) -> str:
        context = "\n\n".join(c.text for c in chunks)
        prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
        # Real impl: call MiMo client.chat(prompt)
        return f"Based on {len(chunks)} retrieved chunks: <answer>"
