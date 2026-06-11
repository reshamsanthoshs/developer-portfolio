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




## Building Conversational History

**Step 1: Understand the Problem**

    Without history:

    User: What is the area of a rectangle with sides 5 and 6?
    AI: 30

    User: What about one with sides 4 and 3?
    AI: What does "one" refer to?

    The second request fails because the model only sees:

    [
        {"role": "user", "content": "What about one with sides 4 and 3?"}
    ]

    It has no idea what happened before.


**Step 2: Store Previous Messages**

    Create a list:

    conversation = []

    Every message exchanged gets added to it.

    Example:

    conversation = [
        HumanMessage(content="What is the area of a rectangle with sides 5 and 6?")
    ]

**Step 3: Send History to the Agent**9

    Instead of:

    response = agent.invoke({
        "messages": [
            HumanMessage(content=query)
        ]
    })

    send the entire conversation:

    response = agent.invoke({
        "messages": conversation
    })

    Now the model sees everything.

**Step 4: Save the Agent Response**

    After invocation:

    response = agent.invoke({
        "messages": conversation
    })

    LangChain returns:

    response["messages"]

    which contains:

    HumanMessage(...)
    AIMessage(...)
    ToolMessage(...)
    AIMessage(...)

    Store it:

    conversation = response["messages"]

**Step 5: Add the Next User Question**
    conversation.append(
        HumanMessage(
            content="What about one with sides 4 and 3?"
        )
    )

    Now history becomes:

    Human: What is area of 5 and 6?
    AI: 30

    Human: What about one with sides 4 and 3?
    Step 6: Invoke Again
    response = agent.invoke({
        "messages": conversation
    })

    The model now understands:

    "What about one"

    means

    "another rectangle"

    because previous context exists.