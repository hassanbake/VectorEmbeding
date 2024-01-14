import os
from dotenv import load_dotenv
from openai import OpenAI
from astrapy.db import AstraDB

def main():
    load_dotenv()

    client = OpenAI()

    response = client.embeddings.create(
        input="Hello, I am Roozbeh and I work as a Developer in a company called Tadbir in Iran.",
        model="text-embedding-ada-002"
    )

    print(response.data[0].embedding)

    token = os.environ.get("ASTRA_DB_APPLICATION_TOKEN")
    api_endpoint = os.environ.get("ASTRA_DB_API_ENDPOINT")

    db = AstraDB(
        token = token,
        api_endpoint = api_endpoint
    )

    print(f"Connected to Astra DB: {db.get_collections()}")


if __name__ == "__main__":
    main()