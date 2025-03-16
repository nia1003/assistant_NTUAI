from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter

app = FastAPI()

# Enable CORS to handle OPTIONS requests properly
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Change this for production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],
)

# Load and process text
with open("../data/113-2 NTUAI 大小事 .txt", "r", encoding="utf-8") as file:
    text = file.read()

text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_text(text)

embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
vectorstore = FAISS.from_texts(texts, embeddings)

qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY")),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask_question(data: Question):
    try:
        answer = qa.run(data.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.options("/ask")
async def options_ask(request: Request):
    return Response(
        status_code=200,
        headers={
            "Access-Control-Allow-Origin": "*",  # Adjust as needed
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "*",
        }
    )
