import ollama

model = "llama3.2"
print("Welcome to the Role-Based Prompt Chatbot powered by Ollama! and model is " + model)


role_based_context = """
You are an Automotive expert, Analyst and a global vehicle database system.
You answer all the questions related to cars, vehicles, automotive industry, car manufacturers, car models, specifications, and related topics.
Answer the user questions according to your role.
"""

while True:
    user_prompt = input("\nPlease enter your prompt:\n")

    if user_prompt.lower() in ["exit", "quit"]:
        print("Thank you for using the chatbot!")
        break

    # Role-based prompting:
    # Give the model a direct instruction with the role context.
    role_based_prompt = role_based_context + "\n" + user_prompt

    print("\nThinking........!\n")

    response = ollama.generate(
        model=model,
        prompt=role_based_prompt
    )

    print("The prompt to LLM is:\n" + role_based_prompt)
    print("The response is:\n")
    print(response["response"])
    