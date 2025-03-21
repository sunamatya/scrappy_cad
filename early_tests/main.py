import urllib.request
import os
from urllib.parse import urlparse


def download_file(url):
    """
    Downloads a file from a URL and saves it locally, preserving the original filename.
    """
    try:
        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If filename couldn't be extracted or is empty, generate a default name
        if not filename:
            filename = "downloaded_file"

        # Download the file
        urllib.request.urlretrieve(url, filename)
        print(f"Downloaded '{filename}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
url = input("Enter the URL to search: ") # Replace with the actual URL of the file
download_file(url)