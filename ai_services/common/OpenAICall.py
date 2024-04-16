from openai import OpenAI
import os

#If env variable is OPENAI_API_KEY the api_key parameter is optional! 
#Below is just for illustration in case we want to use a differnt env variable.
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

#print(completion.choices[0].message)

def get_completion(prompt, model="gpt-4-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    completion = client.chat.completions.create(model=model, messages=messages, response_format={"type": "json_object"})
    return completion.choices[0].message.content

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500):
    response = client.chat.completions.create (model=model, messages=messages, temperature=temperature, max_tokens=max_tokens)
    return response.choices[0].message.content

def get_completion_and_token_counts(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500):
    response = client.chat.completions.create (
        model=model, 
        messages=messages, 
        temperature=temperature,
        max_tokens=max_tokens)
    content = response.choices[0].message.content
    response.usage.prompt_tokens
    token_dict = {
        'prompt_tokens':response.usage.prompt_tokens,
        'completion_tokens':response.usage.completion_tokens,
        'total_tokens':response.usage.total_tokens
    }
    return content, token_dict

def get_moderated_response (prompt):
    response = client.moderations.create(input=prompt)
    return response.results[0]
