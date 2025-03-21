# import webbrowser
# import pyautogui as py
# import time
# import requests
# from bs4 import BeautifulSoup
#
#
#
# def open_first_three_links(query):
#     search_url = f"https://www.google.com/search?q={query}"
#     response = requests.get(search_url)
#     response.raise_for_status()
#     soup = BeautifulSoup(response.content, "html.parser")
#     link_elements = soup.find_all("a")
#
#     count = 0
#     for link_element in link_elements:
#         href = link_element.get("href")
#         if href and href.startswith("http"):
#             webbrowser.open_new_tab(href)
#             count += 1
#         if count >= 3:
#             break
#
# if __name__ == "__main__":
#     search_query = input("Enter your search query: ")
#     #open_first_three_links(search_query)
#     # initial search
#     webbrowser.open("https://www.google.com")
#     time.sleep(3)
#
#     py.write(search_query, interval=0.1)
#
#     py.keyDown('return')
#     response = requests.get(search_url)
#     response.raise_for_status()
#     soup = BeautifulSoup(response.content, "html.parser")
#     link_elements = soup.find_all("a")
#
#     count = 0
#     for link_element in link_elements:
#         href = link_element.get("href")
#         if href and href.startswith("http"):
#             webbrowser.open_new_tab(href)
#             count += 1
#         if count >= 3:
#             break
import webbrowser
import time
import pyautogui as py
import requests
from bs4 import BeautifulSoup

search_query = input("Enter your search query: ")

# Open Google search page
webbrowser.open("https://www.google.com")
time.sleep(3)

# Type the query and press enter
py.write(search_query, interval=0.1)
py.press('enter')
time.sleep(3)  # Wait for search results to load

# Perform a search request to get search results in text format
search_url = f"https://www.google.com/search?q={search_query}&num=5"
headers = {"User-Agent": "Mozilla/5.0"}  # Imitate a browser request
response = requests.get(search_url, headers=headers)
response.raise_for_status()

# Parse search results
soup = BeautifulSoup(response.text, "html.parser")

# Find all search result links
link_elements = soup.select("a[href]")  # Select all anchor tags with href attribute

count = 0
for link_element in link_elements:
    href = link_element["href"]
    if href.startswith("/url?q="):  # Google wraps links in /url?q=
        link = href.split("/url?q=")[1].split("&")[0]  # Extract the actual link
        if "google.com" not in link:  # Avoid Google internal links
            webbrowser.open_new_tab(link)
            count += 1
        if count >= 3:
            break
