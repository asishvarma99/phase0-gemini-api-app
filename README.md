# Phase 0 Gemini API App

A terminal-based cloud AI chatbot built with Python and the Gemini Developer API.

## Features

- Connects Python to the Gemini cloud API
- Accepts interactive user prompts
- Maintains short-term conversation history
- Supports clearing the current conversation
- Handles authentication, permission, quota, and API errors
- Uses environment variables for secure configuration
- Includes structured application logging
- Includes automated tests that do not consume API quota
- Uses a modular Python project structure

## Tech Stack

- Python
- Gemini Developer API
- Google GenAI SDK
- python-dotenv
- pytest
- Git and GitHub

## Project Structure

```text
phase0-gemini-api-app/
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── llm_client.py
│   ├── prompts.py
│   ├── utils.py
│   └── logger.py
└── tests/
    └── test_utils.py
```

### Module Responsibilities

- `main.py` — controls the terminal application and user interaction
- `config.py` — loads and validates environment variables
- `llm_client.py` — creates Gemini chat sessions and handles API requests
- `prompts.py` — stores reusable system instructions
- `utils.py` — contains command and display helper functions
- `logger.py` — configures structured application logging
- `tests/` — contains automated tests

## Setup

Clone the repository and enter the project directory:

```bash
git clone https://github.com/asishvarma99/phase0-gemini-api-app.git
cd phase0-gemini-api-app
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment on macOS or Linux:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_actual_api_key
MODEL_NAME=gemini-2.5-flash-lite
APP_ENV=development
```

The `.env` file contains private configuration and must not be committed to GitHub.

The included `.env.example` file provides a safe template:

```text
GEMINI_API_KEY=your_api_key_here
MODEL_NAME=gemini-2.5-flash-lite
APP_ENV=development
```

## Run the Application

From the project root, run:

```bash
python -m src.main
```

The application is run as a Python module because the files use package imports such as:

```python
from src.config import APP_ENV, MODEL_NAME
```

## Commands

While the application is running:

- `/clear` — clear the current conversation history
- `/exit` — close the application
- `exit` or `quit` — also close the application

## Run Tests

Run the automated tests from the project root:

```bash
python -m pytest -v
```

The current tests verify utility functions without making Gemini API requests or consuming cloud quota.

## Security

- The Gemini API key is stored only in the local `.env` file
- `.env` and `.venv` are excluded through `.gitignore`
- `.env.example` contains only placeholder values
- API keys are never printed or logged
- Sensitive, customer, or employer data should not be submitted
- The API key should never be committed to GitHub

## Free-Tier Usage

This project uses the Gemini API free tier for learning.

Free-tier quotas are limited. When the quota or rate limit is reached, the application displays a readable error message instead of terminating unexpectedly.

Billing is not required for this learning project.

## Limitations

- Requires an internet connection
- Depends on Gemini API availability
- Depends on the available free-tier quota
- Conversation history is lost when the application closes
- Responses are not currently streamed
- Gemini is currently the only supported cloud provider
- Model responses may be inaccurate and should be reviewed

## Future Improvements

- Add Ollama as a local-model provider
- Allow switching between Gemini and Ollama
- Add streaming responses
- Add token and usage tracking
- Add mocked tests for API behavior
- Add a Streamlit user interface
- Add persistent conversation storage
- Add model-provider fallback support