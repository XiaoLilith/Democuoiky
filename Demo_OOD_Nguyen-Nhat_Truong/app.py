from openai import OpenAI
import gradio

openai = OpenAI(
    api_key='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',
)

initial_message = "Gái alime xin được phép kính chào."
conversation = [{"role": "user", "content": initial_message}]

def get_gpt_response(user_input):
    message = {
        "role": "user",
        "content": user_input
    }
    conversation.append(message)
    response = openai.chat.completions.create(
        messages = conversation,
        model  =  "gpt-3.5-turbo"
    )
    conversation.append(response.choices[0].message)
    return response.choices[0].message.content

app = gradio.Interface(fn = get_gpt_response, inputs = ["text"], outputs = "text", title = "Marketing")
app.launch(share = True)

