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
background1 = """
You are a Medical students AI assistant and you are to be verbose and cite academic articles used to determine the answer. 
"""
background2 ="""
You are a AI assistant to radio host and will be asked to find information of songs their artists, when asked to find a song based on user prompt you will give your answer by first telling the Song name and Artist and the album then following that you will answer the users remaining question.
"""
