import ollama

print("Welcome to the Ollama powered Chat Bot!")

# 1. Define your One-Shot example here
# This gives the model a single concrete example of the desired response style/format
one_shot_messages = [
    {
        "role": "user",
        "content": " Brand: Honda | Country: Japan",
    },
    {
        "role": "assistant",
        "content": "Honda is a Japanese automotive manufacturer.",
    },
]

while True:
    user_input = input(
        "\nEnter your prompt here (or 'quit' or 'exit' or 'q' to exit): \n"
    )
    if user_input.lower() in ["quit", "exit", "q"]:
        break

    print("\nThinking to answer........!")

    # 2. Append the current user prompt to the one-shot context
    current_conversation = one_shot_messages + [
        {"role": "user", "content": user_input}
    ]

    # 3. Use ollama.chat instead of generate to handle structured roles
    response = ollama.chat(model="llama3.2", messages=current_conversation)

    # 4. Extract and print the response text
    print(response["message"]["content"])
