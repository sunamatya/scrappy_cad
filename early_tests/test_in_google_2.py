# import time
# import webbrowser
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
#
# # Set up the Selenium WebDriver
# options = webdriver.ChromeOptions()
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
#
# search_query = input("Enter your search query: ")
#
# # Perform a DuckDuckGo search
# driver.get("https://duckduckgo.com/")
# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys(search_query)
# search_box.send_keys(Keys.RETURN)
#
# time.sleep(3)  # Wait for results to load
#
# # Extract the top 3 result links
# search_results = driver.find_elements(By.XPATH, "//a[contains(@class, 'result__a')]")
#
# count = 0
# for result in search_results:
#     link = result.get_attribute("href")
#     if link:
#         print(f"Opening: {link}")
#         webbrowser.open_new_tab(link)
#         count += 1
#     if count >= 3:
#         break
#
# driver.quit()


# import time
# import webbrowser
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
#
# # Set up the Selenium WebDriver
# options = webdriver.ChromeOptions()
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
#
# search_query = input("Enter your search query: ")
#
# # Open DuckDuckGo and search
# driver.get("https://duckduckgo.com/")
# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys(search_query)
# search_box.send_keys(Keys.RETURN)
#
# time.sleep(3)  # Wait for results to load
#
# # Extract the top 3 result links
# search_results = driver.find_elements(By.CSS_SELECTOR, ".result__url")
#
# count = 0
# for result in search_results:
#     link = result.get_attribute("href")
#     if link:
#         print(f"Opening: {link}")
#         webbrowser.open_new_tab(link)
#         count += 1
#     if count >= 3:
#         break
#
# # Close the browser after some time
# time.sleep(5)
# driver.quit()


import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Set up the Selenium WebDriver
options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

search_query = input("Enter your search query: ")

# Open DuckDuckGo and perform the search
driver.get("https://duckduckgo.com/")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

time.sleep(3)  # Wait for results to load

# Extract the top 3 result links
search_results = driver.find_elements(By.CSS_SELECTOR, "a.result__a")

count = 0
for result in search_results:
    link = result.get_attribute("href")
    if link:
        print(f"Opening: {link}")
        webbrowser.open_new_tab(link)
        count += 1
    if count >= 3:
        break

# Close the browser
time.sleep(5)
driver.quit()


