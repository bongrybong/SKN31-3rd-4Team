from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

def create_vectorstore(docs):

    embedding = OpenAIEmbeddings(
        model="text-embedding-3-large"
    )

    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embedding,
        persist_directory="./medicine_db"
    )

    return vectorstore


def load_vectorstore():

    embedding = OpenAIEmbeddings(
        model="text-embedding-3-large"
    )

    embeded = Chroma(
        persist_directory="./medicine_db",
        embedding_function=embedding
    )
    
    return embeded