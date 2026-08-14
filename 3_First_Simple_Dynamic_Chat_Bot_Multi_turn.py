import ollama 

print("Welcome to Ollama powered simple chat-bot! Type 'exit' or 'quit' to end the chat session.")

while True:
    prompt = input("Please enter your prompt: \n")
    
    if prompt.lower() in ['exit', 'quit']:
        print("Thank you for using the chat-bot!")
        break

    response = ollama.generate(
        model = "llama3.2", # llama     
        prompt = prompt
        )

    print("Thinking........!\n")
    print("The response is: \n", response['response'])

