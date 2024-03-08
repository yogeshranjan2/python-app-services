from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

#Make this configurable
persist_dir = "/Users/apple/dev/python-app-services/ai_services//data/chroma"
embedding = OpenAIEmbeddings()

def load_embeddings_to_vectordb(split_docs):
    vectordb = Chroma(persist_directory=persist_dir,embedding_function=embedding)

    print (f"Vectordb from disk - {vectordb}")
    if (vectordb is None or vectordb._collection.count() == 0):
        print("vectordb not present on disk. Loading the file to vector db")
        #If not on disk, then load it.
        vectordb = Chroma.from_documents(
            documents=split_docs,
            embedding=embedding,
            persist_directory=persist_dir
        )
        vectordb.persist()
    return vectordb

def get_vectordb():
    vectordb = Chroma(persist_directory=persist_dir,embedding_function=embedding)
    print (f"Vectordb from disk - {vectordb}")
    if (vectordb is None or vectordb._collection.count() == 0):
        print("vectordb not present on disk. Load the file to vector db")
    return vectordb


