from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import time

app = FastAPI()

class IngestionRequest(BaseModel):
    document_path: str

@app.post("/ingest")
async def ingest_document(request: IngestionRequest):
    document_path = request.document_path

    print(f"Received request to process: {document_path}")

    # Check if file exists before processing
    if not os.path.exists(document_path):
        print(f"Error: File not found at {document_path}")
        raise HTTPException(status_code=404, detail="File not found")
    print(f"Processing document: {document_path}")
    time.sleep(3)

    return {"status": "processed", "document": document_path}