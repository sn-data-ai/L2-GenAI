import ollama

print("Welcome to the Zero-Shot Prompt Chatbot!")
print("Type 'exit' or 'quit' to end the chat session.")

while True:
    user_prompt = input("\nPlease enter your prompt:\n")

    if user_prompt.lower() in ["exit", "quit"]:
        print("Thank you for using the chatbot!")
        break

    # Zero-shot prompting:
    # Give the model a direct instruction without any examples.
    zero_shot_prompt = f"""
You are a helpful AI assistant.

Perform the following task directly and clearly.
Do not rely on any provided examples.

Task:
{user_prompt}
"""

    print("\nThinking........!\n")

    response = ollama.generate(
        model="llama3.2",
        prompt=zero_shot_prompt
    )

    print("The response is:\n")
    print(response["response"])