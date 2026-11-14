import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from app.agents.tools import search_compliance_guidelines, audit_operational_records


load_dotenv(Path(__file__).resolve().parent / ".env")


def get_compliance_agent():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable set nahi hai.")

    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        groq_api_key=api_key,
        temperature=0.1,
    )

    tools = [search_compliance_guidelines, audit_operational_records]

    system_prompt = (
        "You are an Autonomous Regulatory Compliance and Audit Agent. "
        "Review departmental records using your tools, cross-reference with safety guidelines, "
        "identify violations, and present a structured audit summary report."
    )

    agent = create_react_agent(llm, tools=tools, prompt=system_prompt)
    return agent
   