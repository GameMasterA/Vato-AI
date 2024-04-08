import openai

openai.api_key = "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"

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "user", "content": system_msg})

print("Your new assistant  is ready!")
while input != "quit()":
    message = input("")
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "user", "content": reply})
    print("\n" + reply + "\n")