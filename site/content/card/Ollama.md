---
created: 2024-01-19 15:58:35-08:00
title: Ollama
updated: 2024-02-01 05:52:45-08:00
---

Local [LLM](Large%20Language%20Model.md) host.

## Installation

Linux and WSL. macOS is a direct download, and Windows native is not there yet.

````sh
curl https://ollama.ai/install.sh | sh
````

## Usage

````sh
ollama run MODEL_NAME
````

This runs an interactive session with the model, downloading it first if need be. Capabilities are limited by available models and your hardware. None of them are GPT-4 or anything — not on my machine anyways — but it's far more responsive than hosted solutions.

Full list of supported models [here](https://ollama.ai/library).

Also provides a REST server, but I haven't messed with that yet.

## Integrations

* [ollama-python](https://github.com/ollama/ollama-python): official library for [Python](Python.md)
* [ollama-js](https://github.com/ollama/ollama-js): official library for [JavaScript](JavaScript.md)
* [ollama-ai](https://github.com/gbaptista/ollama-ai): support for [Ruby](Ruby.md)

## Related

* https://ollama.ai
* [GitHub - ollama/ollama](https://github.com/ollama/ollama)