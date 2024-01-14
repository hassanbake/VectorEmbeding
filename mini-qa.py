import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import AstraDB

from datasets import load_dataset

load_dotenv()

token = os.environ.get("ASTRA_DB_APPLICATION_TOKEN")
api_endpoint = os.environ.get("ASTRA_DB_API_ENDPOINT")

# llm = OpenAI()
embeddings = OpenAIEmbeddings()

astra_db = AstraDB(
    embedding=embeddings,
    collection_name = "mini_qa_collection",
    token=token, 
    api_endpoint=api_endpoint
)

print("loading data from huggingface...")
my_dataset = load_dataset("Biddls/Onion_News", split="train")
headlines = my_dataset["text"][:50]

print("Adding to database...")
astra_db.add_texts(headlines)
print("%i headlines inserted")
