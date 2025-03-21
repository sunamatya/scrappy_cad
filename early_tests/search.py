import requests
from bs4 import BeautifulSoup
import re


def search_items_in_url(url, search_terms):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        text_content = soup.get_text(separator=' ', strip=True)
        results = {}
        for term in search_terms:
            matches = re.findall(r'\b' + re.escape(term) + r'\b', text_content, re.IGNORECASE)
            results[term] = len(matches)
        return results
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    url = input("Enter the URL to search: ")
    search_terms_input = input("Enter search terms (comma-separated): ")
    search_terms = [term.strip() for term in search_terms_input.split(',')]

    if not url:
        print("URL cannot be empty.")
    elif not search_terms:
        print("Search terms cannot be empty.")
    else:
        results = search_items_in_url(url, search_terms)
        if results:
            print("\nSearch Results:")
            for term, count in results.items():
                print(f"- '{term}': {count} occurrences")