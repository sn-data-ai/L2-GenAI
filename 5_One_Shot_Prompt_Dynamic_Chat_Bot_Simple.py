import ollama

print("Welcome to the One-Shot Prompt Chatbot!")
print("Type 'exit' or 'quit' to end the chat session.")

while True:
    user_prompt = input("\nPlease enter your prompt:\n")

    if user_prompt.lower() in ["exit", "quit"]:
        print("Thank you for using the chatbot!")
        break

    # One-shot prompting:
    # Give the model a direct instruction with one example.
    one_shot_prompt = "This is a one-shot prompt. Please respond to the following user input referring to the given example - Fruit: Apple, Color:Green:\n" + user_prompt

    print("\nThinking........!\n")

    print("The prompt to LLM is:\n" + one_shot_prompt)

    response = ollama.generate(
        model="llama3.2",
        prompt=one_shot_prompt
    )

    print("The response is:\n")
    print(response["response"])