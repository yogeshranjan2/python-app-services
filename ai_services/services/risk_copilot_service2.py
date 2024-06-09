from langchain_openai import ChatOpenAI 
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
import json

from common.OpenAICall import get_completion
from common.policies import policy_details, current_risks_controls

#Define a data structure for JSON
class RiskData (BaseModel):
    riskTitle: str = Field (description="The title of the risk")
    riskDescription: str = Field(description="The description of the risk")
    riskCategory: str = Field(description="Category associated to the risk")
    riskControls: list[str] = Field(description="List of controls associated to the risk")

class RiskDataList(BaseModel):
    riskList: list[RiskData]

class RiskGap (BaseModel):
    riskTitle: str = Field (description="The title of the risk")
    weakArea: str = Field(description="The weak area of the risk.")
    weakControls: str = Field(description="The weaker contols of the risk")
    newControls: str = Field(description="The new controls to be added to the risk")


information_security_policy_text = policy_details.information_security_policy_text
software_development_policy_text = policy_details.application_development_policy_text

model = ChatOpenAI()

def getPolicyContent (policyName):
    if "Information Security" in policyName:
        policy_text = information_security_policy_text
    elif "Software Development" in policyName:
        policy_text = software_development_policy_text
    else:
        policy_text = ""
    return policy_text

generate_risks_controls_prompt_template = """
    You are an expert at identifying risks and its associated controls related to business process and policy in financial services. 
    Provide me {riskCount} operational risks related to the policy below delimited by triple backticks. The risk should be associated with 
    broad risk categories - Buiness process failure, Technology failure and Security breach. For each risk come up control measures also. 
    An effective control meausure should minimize the risk. If there are more than one control measures mention as a list.

    Policy content:
    ```{policy_text}```

    Generate the output in JSON format with the following format instruction: 
    {format_instructions}
    """

def generatePrompt (riskCount, policyName):
    if "Information Security" in policyName:
        policy_text = information_security_policy_text
    elif "Software Development" in policyName:
        policy_text = software_development_policy_text
    else:
        policy_text = ""

    generate_risks_controls_prompt = f"""
    You are an expert at identifying risks and its associated controls related to business process and policy in financial services. 
    Provide me {riskCount} operational risks related to the policy below delimited by triple backticks. The risk should be associated with 
    broad risk categories - Buiness process failure, Technology failure and Security breach. For each risk come up control measures also. 
    An effective control meausure should minimize the risk. If there are more than one control measures mention as a list.

    Policy content:
    ```{policy_text}```

    Generate the output in JSON format with the following keys: 
        RiskTitle, RiskDescription, RiskCategory, RiskControls.

    There should be {riskCount} risk entries in the JSON output.
    """

    return generate_risks_controls_prompt

def generatePromptForMissingRisks(policyName, current_risks_str):
    if "Information Security" in policyName:
        policy_text = information_security_policy_text
    elif "Software Development" in policyName:
        policy_text = software_development_policy_text
    else:
        policy_text = ""

    generate_missing_risks_controls_prompt = f"""
    You are an expert at identifying risks and its associated controls related to business process and policy in financial services. 
    We currenly have a set of risks and controls as descibed below under section Current risk and conrtols. 

    Current risk and controls: 
    {current_risks_str}

    The policy document is mentioned below under section Policy content delimited by triple backticks.

    Policy content:
    ```{policy_text}```

    Identify missing risks and controls associated to the above policy. The missing risks should be associated with the
    same broad risk categories - Buiness process failure, Technology failure and Security breach. For each risk come up control measures also. 
    An effective control meausure should minimize the risk. If there are more than one control measures mention as a list.

    Identify at least 2 missing risks.

    Generate the output in JSON format as below.

    RiskTitle: <Title of the risk>
    RiskDescription: <short description of the risk>
    RiskCategory: <Risk categiry>
    RiskControls: <list any new controls to be added>

    """

    return generate_missing_risks_controls_prompt


def generateRisksAndControls(riskCount, policyName):
    policy_text = getPolicyContent(policyName=policyName)
    parser = JsonOutputParser(pydantic_object=RiskDataList)
    prompt = PromptTemplate(template=generate_risks_controls_prompt_template,
                            input_variables=["riskCount", "policy_text"],
                            partial_variables={"format_instructions": parser.get_format_instructions()}
                            )
    chain = prompt | model | parser
    response = chain.invoke({"riskCount": riskCount, "policy_text" : policy_text})
    #The above response is a dictionary with one key/value pair. Returning the first value.
    return next(iter(response.values()))
    

def generateOpEventAnalyisPrompt (opEventDescription, risks_str):
    op_event_analysis_prompt = f"""
    You are an expert at identifying risks and its associated controls related to business process and policy in financial services.
    Our current identified risks and controls in JSON format are below:

    Current risk and controls: {risks_str}

    There is an incident which indicates some weakness in our risks and controls. The inciddent description is below

    Incident description:
    {opEventDescription}

    Identify at least 5 risks and controls can be potentially weak. If there is a missing control, then mention a new control which
    can be added to the risk. In case there is no relevant risk for the incident, just say No relevant Risk. If there are multiple
    risks which are weak, then mention each risk as one item.

    Output a JSON array response in the below format. If there are more than one weak risks, then mention each risk in the below 
    format as a list in the JSON array.

    RiskTitle: <Risk title from our risk and controls>
    WeakArea: <what is the weakness here>
    WeakControls: <What controls are weak>
    NewControls: <list any new controls to be added>

    """
    return op_event_analysis_prompt

def analyseRCSAGaps (opEventDescription):
    currentRiskControls = current_risks_controls.information_security_risks_controls
    #convert the above list to string
    risk_list = list(map(lambda risk: json.dumps(risk, indent=4), currentRiskControls))
    risks_str = ", ".join(risk_list)
    op_event_analysis_prompt = generateOpEventAnalyisPrompt(opEventDescription, risks_str)
    print(risks_str)
    response = get_completion(op_event_analysis_prompt)
    print (response)
    json_output_dict = json.loads(response)
    keys = list(json_output_dict)

    if (len(keys) != 1) :
        print ('inside if.......')
        risk_list = [json_output_dict]
        return risk_list
    else:
        print ('inside else.....')
        print (json_output_dict)
        return json_output_dict[keys[0]]

def getCurrentRisksAndControls():
    return current_risks_controls.information_security_risks_controls

def generateMissingRisksAndControls(policyName):
    currentRiskControls = current_risks_controls.information_security_risks_controls
    #convert the above list to string
    risk_list = list(map(lambda risk: json.dumps(risk, indent=4), currentRiskControls))
    current_risks_str = ", ".join(risk_list)
    prompt = generatePromptForMissingRisks(policyName, current_risks_str)
    response = get_completion(prompt)
    json_output_dict = json.loads(response)
    keys = list(json_output_dict)
    #Below is tactical solution to return list when only one risk is returned by the model
    if (len(keys) != 1) :
        print ('inside if.......')
        risk_list = [json_output_dict]
        return risk_list
    else:
        print ('inside else.....')
        print (json_output_dict)
        return json_output_dict[keys[0]]


