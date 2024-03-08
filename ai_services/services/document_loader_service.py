from enum import Enum
from langchain_community.document_loaders import WebBaseLoader, CSVLoader, PyPDFLoader, UnstructuredWordDocumentLoader, TextLoader
from langchain_core.documents.base import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

from common.document_type import DocumentType
from ai_services.services.vectordb_service import load_embeddings_to_vectordb

def load_document (docType, documentUri):
    doc_pages = []
    match docType.value:
        case DocumentType.WEB_PAGE.value:
            loader = WebBaseLoader(documentUri)
            doc_pages = loader.load()
            print (f"Loaded web page has {len(doc_pages)} pages. Meta data is {doc_pages[0].metadata}")
        case DocumentType.PDF.value:
            loader = PyPDFLoader(documentUri)
            doc_pages = loader.load()
            print (f"Loaded PDF document has {len(doc_pages)} pages. Meta data is {doc_pages[0].metadata}")
        case DocumentType.CSV.value:
            loader = CSVLoader(documentUri)
            doc_pages = loader.load()
            print (f"Loaded CSV document has {len(doc_pages)} pages. Meta data is {doc_pages[0].metadata}")
        case DocumentType.WORD.value:
            loader = UnstructuredWordDocumentLoader(documentUri, mode="elements")
            doc_pages = loader.load()
            print (f"Loaded word document has {len(doc_pages)} pages. Meta data is {doc_pages[0].metadata}")
        case DocumentType.TXT.value:
            loader = TextLoader(documentUri)
            doc_pages = loader.load()
            print (f"Loaded TXT document has {len(doc_pages)} pages. Meta data is {doc_pages[0].metadata}")
        case _:
            print ('Invalid doc type passed. Supported document types are web page, pdf, csv, word doc and txt')
    return doc_pages

def split_doc_into_chunks(docPages): 
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 120,
        separators=["\n\n", "\n", "(?<=\. )", " ", ""]
    )
    split_docs = text_splitter.split_documents(docPages)
    print (f"Split document has {len(split_docs)} pages.")  
    return split_docs

def load_embed_store_doc(docType:Enum, documentUri):
    doc_pages = load_document(docType, documentUri)
    split_docs = split_doc_into_chunks(doc_pages)
    load_embeddings_to_vectordb(split_docs)