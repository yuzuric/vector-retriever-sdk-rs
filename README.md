# Vector Retriever Sdk Rs

> Knowledge-grounded QA pipeline with incremental indexing and relevance feedback loops powered by Xiaomi MiMo.

`rag` `embeddings` `vector-search` `mimo`

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Built with MiMo](https://img.shields.io/badge/Built%20with-Xiaomi%20MiMo-orange.svg)](https://platform.xiaomimimo.com)

## Overview

`vector-retriever-sdk-rs` is built on top of [Xiaomi MiMo](https://platform.xiaomimimo.com), the open-source large language model series from Xiaomi. The project demonstrates how to integrate MiMo into production systems using its OpenAI-compatible API.

## Use Cases

- **Internal knowledge bases** — answer questions grounded in company docs
- **Documentation chatbots** — ground answers in product manuals and FAQs
- **Research assistants** — synthesize answers across academic papers
- **Customer support automation** — pull from past tickets and runbooks

## Quick Start

### Install

```bash
pip install -e .
# or for development
pip install -e ".[dev]"
```

### Run

```bash
export MIMO_API_KEY=your_key_here
python main.py
```

### Programmatic Use

```python
import asyncio
from vector_retriever_sdk_rs.client import MiMoClient

async def example():
    client = MiMoClient(model="mimo-7b", api_key="...")
    response = await client.chat("Hello, MiMo!")
    print(response["content"])

asyncio.run(example())
```

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│  Application │───▶│  vector_retriev │───▶│  Xiaomi MiMo    │
│              │     │  (this repo) │     │  (LLM API)      │
└─────────────┘     └──────────────┘     └─────────────────┘
                            │
                            ▼
                    ┌──────────────┐
                    │  Local State │
                    │  / Cache     │
                    └──────────────┘
```

The library wraps the MiMo HTTP API and exposes a high-level interface tuned for the rag use case. Configuration is YAML-first with environment variable overrides for secrets.

## Configuration

`config.yaml`:

```yaml
model: ${MIMO_MODEL:-mimo-7b}
api_key: ${MIMO_API_KEY}
max_parallel: 4
```

Environment variables override file values. See `config.yaml` in the repo root for the full schema.

## Development

```bash
# Run tests
pytest -v

# Lint
ruff check .
```

CI runs on every push and PR via GitHub Actions (`.github/workflows/ci.yml`).

## Project Structure

```
vector-retriever-sdk-rs/
├── README.md
├── LICENSE
├── pyproject.toml
├── config.yaml
├── main.py
├── src/vector_retriever_sdk_rs/
│   ├── retriever.py
│   ├── client.py
│   └── config.py
├── tests/
│   └── test_retriever.py
└── .github/
    └── workflows/
        └── ci.yml
```

## Why MiMo?

Xiaomi MiMo is a strong open-weight LLM with competitive reasoning performance and an OpenAI-compatible API. Choosing MiMo as the backend gives this project:

- **Cost-effective inference** — significantly cheaper than proprietary frontier models for comparable quality
- **Open licensing** — weights and code are available under permissive terms
- **Strong reasoning** — competitive performance on math, code, and multi-step planning benchmarks
- **Production-ready API** — drop-in replacement for OpenAI client libraries

## Contributing

Contributions welcome. Please:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Add tests for new behavior
4. Open a PR with a clear description

See `.github/workflows/ci.yml` for the checks that must pass.

## License

MIT — see [LICENSE](LICENSE).

## Acknowledgments

Built with [Xiaomi MiMo](https://platform.xiaomimimo.com). This project is part of the MiMo 100T Token Plan ecosystem submission.
