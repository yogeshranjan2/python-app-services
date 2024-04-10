from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableBranch

'''
Router chain to route to different chains based on an incoming question
We start with a parent chain which is a context setting chain.
'''
parentChain = (
    PromptTemplate.from_template(
        """
            Given the user question below, classify it as either being about 
            `LangChain`, `Anthropic`, or `Other`. Do not respond with more than one word.
            <question>
            {question}
            </question> 
        """
    )
    | ChatOpenAI()
    | StrOutputParser()
)

# response = parentChain.invoke({"question":"What is differene between Anthropic and langchain?"})
# print (response)

#Create 3 new child chains

langchain_chain = (
    PromptTemplate.from_template(
        """
        You are an expert in langchain.
        Always answer questions starting with "As Harrison Chase told me".
        Respond to the following question:
        Question: {question}
        """
    )
    | ChatOpenAI()
)
anthropic_chain = (
    PromptTemplate.from_template(
        """
        You are an expert in anthropic. \
        Always answer questions starting with "As Dario Amodei told me". \
        Respond to the following question:
        Question: {question}
        """
    )
    | ChatOpenAI()
)
general_chain = (
    PromptTemplate.from_template( 
        """
        Respond to the following question:
        Question: {question}
        """
    )
    | ChatOpenAI()
)

branch = RunnableBranch(
    (lambda x: "anthropic" in x["topic"].lower(), anthropic_chain),
    (lambda x: "langchain" in x["topic"].lower(), langchain_chain),
    general_chain,
)
full_chain = {"topic": parentChain, "question": lambda x: x["question"]} | branch
response = full_chain.invoke({"question": "what is LangChain"})
print (response)