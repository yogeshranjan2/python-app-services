from ai_services.common.document_type import DocumentType
from ai_services.services.document_loader_service import load_embed_store_doc
from ai_services.services.document_qa_service import get_question_answer
import os
from . import api_blueprint

from flask import request, jsonify

@api_blueprint.route('/health-check', methods=['GET'])
def health_check():
    return "AI Service is up and running!"

@api_blueprint.route('/load-web-page', methods=['POST'])
def load_web_page():
    url = request.json['url']
    load_embed_store_doc(DocumentType.WEB_PAGE, url)
    return "Loaded web page in vector db successfully!"

@api_blueprint.route('/load-document', methods=['POST'])
def load_document():
    #docPath = "/Users/apple/dev/python-app-services/ai_services/data/Electric_Vehicle_Population_Data.csv"
    docPath = "/Users/apple/dev/python-app-services/ai_services/data/sec-guide-to-mutual-funds.pdf"
    fileExt = os.path.splitext(docPath)[1]
    if (fileExt.lower().endswith("csv")):
        load_embed_store_doc(DocumentType.CSV, docPath)
    elif (fileExt.lower().endswith("pdf")):
        load_embed_store_doc(DocumentType.PDF, docPath)
    elif (fileExt.lower().endswith("docx")):
        load_embed_store_doc(DocumentType.WORD, docPath)
    elif (fileExt.lower().endswith("txt")):
        load_embed_store_doc(DocumentType.TXT, docPath)
    return "Loaded document in vector db successfully!"

@api_blueprint.route('/query-document', methods=['POST'])
def query_document():
    question = request.json['question']
    answer = get_question_answer(question)
    return answer
