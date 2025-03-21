import ollama

response = ollama.chat(model="llama3", messages=[
    {"role": "system", "content": "You are an AI assistant."},
    {"role": "user", "content": "Generate search queries to find free CAD files (STL, STEP, IGES) online."}
])

print(response['message']['content'])

