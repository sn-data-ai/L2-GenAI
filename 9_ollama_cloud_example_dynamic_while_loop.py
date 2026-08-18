from ollama import Client

# Initialize the Ollama Cloud connection directly with your key
client = Client(
    host="https://ollama.com",
    headers={"Authorization": "Bearer e3262e2343884c5aae08dd588aa390b3.5x5LJDl-jFOz_TuOAQ_BhdrX"}
)

model1 = "gpt-oss:20b-cloud"
model2 = "gpt-oss:120b-cloud"

print(f"--- Ollama Cloud Chat Bot Started using {model1} ---")
print("Type 'quit' or 'exit' to end the program.\n")

while True:
    prompt = input("Enter your prompt: ").strip()
    
    # Check for exit condition (case-insensitive)
    if prompt.lower() in ["quit", "exit"]:
        print("Exiting chat. Goodbye!")
        break
        
    # Skip empty inputs
    if not prompt:
        continue
        
    try:
        print("\nThinking...")
        # Request the cloud model
        response = client.chat(
            model=model1,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Print the response text
        print(f"\nModel: {response['message']['content']}\n")
        print("-" * 40)
        
    except Exception as e:
        print(f"\nAn error occurred: {e}\n")
