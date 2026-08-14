import ollama

model = "llama3.2"
print("Welcome to the Few-Shot Prompt Chatbot powered by Ollama! and model is " + model)


few_shot_prompt_context = """This is a few-shot prompt. Please respond to the following user input referring to the given examples -
    Example 1: Car_Manufacturer_Brand: Honda, Country_of_Origin:Japan,
    Example 2: Car_Manufacturer_Brand: BMW, Country_of_Origin:Germany,
    Example 3: Car_Manufacturer_Brand: Ford, Country_of_Origin:USA
"""

while True:
    user_prompt = input("\nPlease enter your prompt:\n")

    if user_prompt.lower() in ["exit", "quit"]:
        print("Thank you for using the chatbot!")
        break

    # Few-shot prompting:
    # Give the model a direct instruction with multiple examples.
    few_shot_prompt = few_shot_prompt_context + "\n" + user_prompt

    print("\nThinking........!\n")

    response = ollama.generate(
        model=model,
        prompt=few_shot_prompt
    )

    print("The prompt to LLM is:\n" + few_shot_prompt)
    print("The response is:\n")
    print(response["response"])
    