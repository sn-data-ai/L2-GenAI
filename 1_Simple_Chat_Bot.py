import ollama

prompt = "Whats the capital of India?"

response = ollama.generate(
    model = "llama3.2", 
    prompt=prompt
)

print("\nThe input prompt is: \n", prompt)
print("\nThinking to answer........!")
print("\n here is the AI / LLMs response : \n")
print(response['response'])