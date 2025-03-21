import requests

url = "https://example.com/cad_files/my_model.dwg"  # Replace with the actual URL
response = requests.get(url, stream=True)
response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

with open("my_model.dwg", "wb") as file:  # "wb" for writing in binary mode
    for chunk in response.iter_content(chunk_size=8192):  # Iterate over the response in chunks
        if chunk:  # Filter out keep-alive chunks
            file.write(chunk)