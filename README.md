# Learn LangGraph

Monorepo for learning how to build **stateful LLM workflows** with [LangGraph](https://github.com/langchain-ai/langgraph).

It contains two small, practical projects:

- `calculator`: tool-calling arithmetic agent
- `support_email`: customer support workflow with routing and human review

## What Is in This Monorepo

### 1) `calculator` (Beginner project)

A compact project to understand the LangGraph fundamentals:

- graph state
- nodes
- conditional routing
- tool execution loop

How it works:

1. `llm_call` receives messages and decides whether to call a tool.
2. `tool_node` executes one of the arithmetic tools (`add`, `subtract`, `multiply`, `divide`).
3. `should_continue` loops back to the LLM or ends the graph.

Main files:

- `calculator/tools.py`: model setup + tools
- `calculator/state.py`: graph state schema
- `calculator/nodes.py`: node logic
- `calculator/build_compile.py`: build/compile graph, generate image
- `calculator/invoke.py`: runnable example

### 2) `support_email` (Intermediate project)

A larger workflow showing multi-step orchestration:

- read incoming email
- classify intent and urgency
- route to docs search or bug tracking
- draft response
- pause for human approval (`interrupt`)
- resume and send reply

Main files:

- `support_email/state.py`: typed workflow state
- `support_email/compile.py`: graph assembly + memory checkpointer
- `support_email/nodes/*`: business steps (classification, search, response)
- `support_email/run_agent.py`: end-to-end example with resume

## Quick Start

### Requirements

- Python 3.11+ (3.12 recommended)
- virtual environment
- provider API key in `.env`

### Setup

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install langgraph langchain langchain-deepseek langchain-openai python-dotenv ipython taskipy
```

Create `.env` at the project root:

```env
DEEPSEEK_API_KEY=your_key_here
```

## Run

With tasks (from `pyproject.toml`):

```bash
task calculator
task support_email
```

Or directly:

```bash
python -m calculator.invoke
python -m support_email.run_agent
```

To generate the calculator graph image:

```bash
python -m calculator.build_compile
```

## Learning Path

Recommended order:

1. Start with `calculator` to learn LangGraph basics.
2. Move to `support_email` to learn branching, persistence, and human-in-the-loop review.