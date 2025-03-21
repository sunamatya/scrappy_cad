import requests


def get_search_results(query):
    url = f"https://api.parsera.org/v1/parse?query={query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  # Extract CAD file links
    else:
        print("Error:", response.text)
        return None


cad_links = get_search_results("free STL robot parts")
print(cad_links)

import os

def download_cad_file(url, save_path="cad_files/"):
    os.makedirs(save_path, exist_ok=True)
    file_name = url.split("/")[-1]

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(os.path.join(save_path, file_name), "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Downloaded: {file_name}")
    else:
        print("Failed:", url)

for link in cad_links:
    download_cad_file(link)