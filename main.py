"""
RAG pipeline entry point: index docs, retrieve context, generate answers via MiMo.
"""
import asyncio
from pathlib import Path
from vector_retriever_sdk_rs.retriever import VectorRetriever
from vector_retriever_sdk_rs.synthesizer import AnswerSynthesizer
from vector_retriever_sdk_rs.config import load_config


async def main() -> None:
    config = load_config("config.yaml")
    retriever = VectorRetriever(
        index_path=config["index_path"],
        embedding_model=config["embedding_model"],
    )
    synthesizer = AnswerSynthesizer(
        model=config["mimo_model"],
        api_key=config["api_key"],
    )

    # Index documents
    docs = list(Path(config["docs_dir"]).glob("*.md"))
    await retriever.index(docs)

    # Query loop
    query = "How does MiMo handle long-context reasoning?"
    chunks = await retriever.search(query, top_k=5)
    answer = await synthesizer.generate(query, chunks)
    print(f"Q: {{query}}\nA: {{answer}}")


if __name__ == "__main__":
    asyncio.run(main())
