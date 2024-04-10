from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

from ai_services.services.vectordb_service import get_vectordb

def get_question_answer(question):
    vectordb = get_vectordb()
    model = ChatOpenAI()

    # Build prompt
    template = """
    Use the following pieces of context to answer the question at the end. If you don't know the answer, just say 
    that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as 
    possible. Always say "thanks for asking!" at the end of the answer. 
    {context}
    Question: {question}
    Helpful Answer:"""
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

    #Setup QA chain
    qa_chain = RetrievalQA.from_chain_type(
        model,
        retriever=vectordb.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )
    #Invoke the chain
    answer = qa_chain.invoke(question)
    print()
    print (f"Answer result => {answer['result']}")
    print()
    print (f"Answer source documents => {answer['source_documents']}")
    return answer['result']