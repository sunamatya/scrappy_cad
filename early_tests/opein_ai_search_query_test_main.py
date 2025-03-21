#use LLM to generate search queries for the setup
import openai

# Set your OpenAI API key
#free api key downloaded from https://github.com/dan1471/FREE-openai-api-keys
openai.api_key = ""

#check list of open ai models supported
models = openai.Model.list()
print([model["id"] for model in models["data"]])

query_prompt = "Generate a list of search queries to find free CAD files (STL, STEP, IGES) online for Baseplates of different shapes, Cylindrical pipes, Spur Gears and L-brackets"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Specify the LLM model
    messages=[{"role": "system", "content": query_prompt}],
    max_tokens=100
)

search_queries = response["choices"][0]["message"]["content"]
print(search_queries)

