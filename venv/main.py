import openai


openai.api_key  = ('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

#format background like so below
# messages =  [  
# {'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
# {'role':'user', 'content':'tell me a joke'},   
# {'role':'assistant', 'content':'Why did the chicken cross the road'},   
# {'role':'user', 'content':'I don\'t know'}  ]
background1 = """
You are a Medical students AI assistant and you are to be verbose and cite academic articles used to determine the answer. 
"""
background2 ="""
You are a AI assistant to radio host and will be asked to find information of songs their artists, when asked to find a song based on user prompt you will give your answer by first telling the Song name and Artist and the album then following that you will answer the users remaining question.
"""




response = get_completion_from_messages(messages, temperature=1)
print(response)