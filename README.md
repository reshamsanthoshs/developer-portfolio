# Developer Portfolio

This repository contains projects built as part of my learning journey in AI, LangChain, agents, cloud-native technologies, and software engineering.

## LangChain

LangChain is an open-source framework for building applications powered by Large Language Models (LLMs). It provides abstractions for models, prompts, tools, memory, agents, and workflows, enabling developers to build intelligent applications such as chatbots and AI assistants.

## Prerequisites

Before running the projects in this repository, ensure the following are installed:

### Python

Python 3.11+ is recommended.

Verify installation:

```bash
python3 --version
```

### Virtual Environment

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Project Dependencies

Install required Python packages:

```bash
pip install -r requirements.txt
```

### Ollama

Install Ollama for running local language models.

Verify installation:

```bash
ollama --version
```

Pull the required model:

```bash
ollama pull llama3.2
```

Verify the model is available:

```bash
ollama list
```

### Environment Variables

Create a `.env` file if the project requires API keys or other configuration values:

```env
OPENAI_API_KEY=<your-api-key>
```

## Running the Project

Activate the virtual environment:

```bash
source venv/bin/activate
```

Run the application:

```bash
python ReActAgent.py
```

## Learning Goals

* Build AI agents using LangChain
* Understand tool calling and agent workflows
* Explore LangGraph and multi-step reasoning
* Experiment with local LLMs using Ollama
* Build production-ready AI applications
