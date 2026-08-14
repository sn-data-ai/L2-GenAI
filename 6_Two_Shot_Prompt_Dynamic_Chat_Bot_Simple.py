import ollama

print("Welcome to the Two-Shot Prompt Chatbot!")
print("Type 'exit' or 'quit' to end the chat session.")

while True:
    user_prompt = input("\nPlease enter your prompt:\n")

    if user_prompt.lower() in ["exit", "quit"]:
        print("Thank you for using the chatbot!")
        break

    # Two-shot prompting:
    # Give the model a direct instruction with two examples.
    two_shot_prompt = "This is a two-shot prompt. Please respond to the following user input referring to the given examples - Brand: Honda, Country:Japan; Brand: BMW, Country:Germany:\n" + user_prompt

    print("\nThinking........!\n")

    response = ollama.generate(
        model="llama3.2",
        prompt=two_shot_prompt
    )

    print("The prompt to LLM is:\n" + two_shot_prompt)
    print("The response is:\n")
    print(response["response"])