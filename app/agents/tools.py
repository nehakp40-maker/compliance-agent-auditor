import os
import pandas as pd
from langchain.tools import tool
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

@tool
def search_compliance_guidelines(query: str) -> str:
    """Searches compliance rules, safety policies, and statutory regulations via FAISS."""
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
        if os.path.exists("faiss_index"):
            vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
            docs = vector_store.similarity_search(query, k=2)
            return "\n\n".join([doc.page_content for doc in docs])
        return (
            "Standard Regulatory Guidelines:\n"
            "1. Workplace inspection interval must not exceed 30 days.\n"
            "2. Safety PPE compliance score must remain strictly above 70% across all operational units."
        )
    except Exception as e:
        return f"Error retrieving compliance documentation: {str(e)}"

@tool
def audit_operational_records(filter_criteria: str) -> str:
    """Audits departmental operational records and inspection logs for anomalies using Pandas."""
    try:
        data = {
            "record_id": [101, 102, 103, 104],
            "department": ["Manufacturing", "Logistics", "Packaging", "Chemical"],
            "last_inspection_days_ago": [12, 45, 10, 38],
            "ppe_compliance_score": [95, 60, 92, 55],
            "violations_logged": [0, 3, 0, 2]
        }
        df = pd.DataFrame(data)
        
        # Inspection gap > 30 days ya PPE score < 70 non-compliant maana jayega
        non_compliant = df[(df["last_inspection_days_ago"] > 30) | (df["ppe_compliance_score"] < 70)]
        return non_compliant.to_json(orient="records")
    except Exception as e:
        return f"Error querying dataset: {str(e)}"