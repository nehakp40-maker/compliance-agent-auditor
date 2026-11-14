# Autonomous Compliance & Data Auditor

An agentic AI API that audits operational records against regulatory and safety guidelines and returns a structured audit summary report.

## What it does

You send a natural-language query (for example, "Review the departmental records and identify safety violations"). A ReAct-style AI agent decides which tools to call, cross-references the records with the guidelines, identifies violations, and returns an audit report.

## Tech Stack

- Python 3.13
- FastAPI + Uvicorn
- LangGraph (`create_react_agent`)
- LangChain Groq (`openai/gpt-oss-120b`)
- python-dotenv, Pydantic

## Architecture

```
User query -> FastAPI (/api/audit) -> LangGraph ReAct agent
                                        |-> search_compliance_guidelines (tool)
                                        |-> audit_operational_records (tool)
                                        v
                          Structured audit report -> User
```

## Project Structure

```
compliance-agent-auditor/
├── app/
│   ├── main.py              # FastAPI app and endpoints
│   └── agents/
│       ├── orchestrator.py  # Agent setup (LLM, tools, prompt)
│       └── tools.py         # Custom agent tools
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup

1. Clone the repository

```bash
git clone https://github.com/nehakp40-maker/compliance-agent-auditor.git
cd compliance-agent-auditor
```

2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create a `.env` file at `app/agents/.env`

```
GROQ_API_KEY=your_groq_api_key_here
```

Get a free key from https://console.groq.com/keys

5. Run the server

```bash
python -m uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs for the interactive API docs.

## API Endpoints

### `GET /health`

```json
{"status": "healthy", "service": "compliance-agent-auditor"}
```

### `POST /api/audit`

Request:

```json
{
  "query": "Review the departmental records and identify safety violations."
}
```

Response:

```json
{
  "status": "success",
  "audit_report": "**Audit Summary Report – Safety Compliance Review** ..."
}
```

## Future Improvements

- Connect real data sources (CSV/SQLite) and a vector store for guidelines
- Structured JSON reports (violations, severity, recommendations)
- Streamlit frontend
- Deployment (Render / Railway)

## Author

**Neha Patil**
- GitHub: [github.com/nehakp40-maker](https://github.com/nehakp40-maker)
- LinkedIn: [linkedin.com/in/neha-patil-970638372] (https://www.linkedin.com/in/neha-patil-970638372/)