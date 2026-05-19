"""Tests for retriever."""
import pytest
from pathlib import Path
from vector_retriever_sdk_rs.retriever import Chunk, VectorRetriever


def test_chunk_score_sort():
    chunks = [Chunk("a", "x", 0.3), Chunk("b", "y", 0.9), Chunk("c", "z", 0.5)]
    sorted_chunks = sorted(chunks, key=lambda c: c.score, reverse=True)
    assert sorted_chunks[0].doc_id == "b"
    assert sorted_chunks[-1].doc_id == "a"


@pytest.mark.asyncio
async def test_retriever_empty_search(tmp_path: Path):
    r = VectorRetriever(index_path=str(tmp_path), embedding_model="mock")
    results = await r.search("test", top_k=5)
    assert results == []
