import ollama

prompt1 = "Whats the capital of India?"

response1 = ollama.generate(
    model = "llama3.2", 
    prompt=prompt1
)
prompt2 = "List 2 most popular places to visit there."

response2 = ollama.generate(
    model = "llama3.2", 
    prompt=prompt2
)
print("\nThe input prompt is: \n", prompt1)
print("\nThinking to answer........!")
print("\n here is the AI / LLMs response : \n")
print(response1['response'])

print("\nThe input prompt is: \n", prompt2)
print("\nThinking to answer........!")
print("\n here is the AI / LLMs response : \n")
print(response2['response'])