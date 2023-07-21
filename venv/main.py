import openai
import panel as pn  
pn.extension()

panels = []

openai.api_key  = ('OPENAI_API_KEY')

# def get_completion(prompt, model="gpt-3.5-turbo"):
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=0, # this is the degree of randomness of the model's output
#     )
#     return response.choices[0].message["content"]
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]
def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)

context = [ {'role':'system', 'content':"""
You are a Medical students AI assistant and you are to be verbose and cite academic articles used to determine the answer. \
If unsure of the answer you will ask the user clarifying questions. \
You first greet the user, then ask when the question is and what medical field it relates to. \
Allow time to verify your answer with cited academic written pieces. \
Finally ask the user if you answered their question and if they have any more. \
"""} ] 


inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard



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




messages =  context.copy()
messages.append(
{'role':'system', 'content':'create a json summary of the previous food order. Itemize the price for each item\
 The fields should be 1) pizza, include size 2) list of toppings 3) list of drinks, include size   4) list of sides include size  5)total price '},    
)
 #The fields should be 1) pizza, price 2) list of toppings 3) list of drinks, include size include price  4) list of sides include size include price, 5)total price '},    

response = get_completion_from_messages(messages, temperature=0)
print(response)