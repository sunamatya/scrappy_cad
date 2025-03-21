import webbrowser
import requests

API_KEY = "AIzaSyBZQFbTKGhifYv1UR3Klk85f6mAuMx6ICE"
CX = "a172c118df255403b"
search_query = input("Enter your search query: ")

# Google Custom Search API request
url = f"https://www.googleapis.com/customsearch/v1?q={search_query}&key={API_KEY}&cx={CX}"
response = requests.get(url).json()

# Debug: Print the response to check if links are present
print("Full API Response:", response)

# Open the top 3 search result links
count = 0
for item in response.get("items", []):
    link = item["link"]
    print(f"Opening: {link}")
    webbrowser.open_new_tab(link)
    count += 1
    if count >= 3:
        break
