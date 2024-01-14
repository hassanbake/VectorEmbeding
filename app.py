from openai import OpenAI
from dotenv import load_dotenv

def main():
    load_dotenv()
    client = OpenAI()
    response = client.embeddings.create(
        input="Hello, I am Roozbeh and I work as a Developer in a company called Tadbir in Iran.",
        model="text-embedding-ada-002"
    )

    print(response.data[0].embedding)

if __name__ == "__main__":
    main()