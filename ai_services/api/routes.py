from ai_services.common.document_type import DocumentType
from ai_services.services.document_loader_service import load_embed_store_doc
from ai_services.services.document_qa_service import get_question_answer
from ai_services.services.risk_copilot_service import generateRisksAndControls, analyseRCSAGaps, getCurrentRisksAndControls, generateMissingRisksAndControls
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
    #In real app, the file would be passed from a UI or have a preconfigured location on the server.
    #docPath = "ai_services/data/Electric_Vehicle_Population_Data.csv"
    docPath = "ai_services/data/Information-Security-Policy.pdf"
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

@api_blueprint.route('/generate-risks', methods=['GET'])
def generate_risks_and_controls():
    riskCount = request.args.get("count")
    policyName = request.args.get('policy')
    print (f"request parameters {riskCount} {policyName}")
    risks = generateRisksAndControls(riskCount, policyName)
    return risks

@api_blueprint.route('/generate-missing-risks', methods=['GET'])
def generate_missing_risks_and_controls():
    policyName = request.args.get('policy')
    print (f"request parameters {policyName}")
    risks = generateMissingRisksAndControls(policyName)
    return risks

@api_blueprint.route('/get-current-risks', methods=['GET'])
def get_current_risks_and_controls():
    risks = getCurrentRisksAndControls()
    return risks

@api_blueprint.route('/analyse-incident', methods=['POST'])
def analyse_prod_incident():
    opEventDescription = request.json['opEventDescription']
    return analyseRCSAGaps(opEventDescription)


