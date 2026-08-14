import ollama

print("Welcome to the Ollama powered Chat Bot!")
while True:
    prompt = input("Enter your prompt here (or 'quit' or 'exit' or 'q' to exit): \n")
    if prompt.lower() in ['quit','exit','q']:
        break

    response = ollama.generate(
        model = "llama3.2", 
        prompt=prompt
    )

    print("\nThinking to answer........!")
    print(response['response'])