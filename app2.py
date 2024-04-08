import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a coding ai"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5",
        messages = messages        
    )
    ChatGPT_reply = response["choices"][0]["messages"]["content"]
    messages.append({"role": "assistant", "conent": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interfece(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "VATO AI")

demo.launch()