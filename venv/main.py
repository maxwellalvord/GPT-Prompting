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

import panel as pn 
pn.extension()

panels = []

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

def create_summary(_):
    messages =  context.copy()
    messages.append(
    {'role':'system', 'content':'create a json summary of the academic article cited. Itemize it via title, author, year, URL'},    
    )
    response = get_completion_from_messages(messages, temperature=0)
    print(response)