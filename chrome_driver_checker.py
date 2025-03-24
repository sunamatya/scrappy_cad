from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Set up Chrome WebDriver
options = webdriver.ChromeOptions()
#options.add_argument("--headless")  # Run in headless mode

options.add_argument(f"user-data-dir=C:\\Users\\samatya\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("--profile-directory=Default")  # Change if you have multiple profiles
options.add_argument("--disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.89 Safari/537.36")


#C:\Users\samatya\AppData\Local\Google\Chrome\User Data\Default
# Set download directory
download_path = r"C:\Users\samatya\Downloads\CAD_Files"
if not os.path.exists(download_path):
    os.makedirs(download_path)  # Create directory if it doesn’t exist

prefs = {"download.default_directory": download_path}
options.add_experimental_option("prefs", prefs)


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open McMaster-Carr website
driver.get("https://www.mcmaster.com/")

# Wait for the search bar to be visible
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.ID, "SrchEntryWebPart_InpBox")))

# Find the search bar and enter a search query (e.g., "hex bolt")
#search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("hex bolt")
search_box.send_keys(Keys.RETURN)

time.sleep(5)  # Allow time for page to load
print("Search completed.")

# # Click on the first product link
# product_links = driver.find_elements(By.CSS_SELECTOR, ".ListItem a")
# if product_links:
#     product_links[0].click()
#
# time.sleep(3)
#
# # Locate and click the CAD download button
# try:
#     cad_download_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Download CAD')]")
#     cad_download_button.click()
#     print("CAD download initiated.")
# except:
#     print("CAD download button not found.")
# Click the first product link
#product_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ListItem a")))


# Wait for search results container first
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class*=ListItem]")))

# Get product links
product_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[class*=ListItem] a")))

# Debugging: Print the number of products found
print(f"Found {len(product_links)} products.")

if product_links:
    product_links[0].click()
else:
    print("No product found.")
    driver.quit()
    exit()

time.sleep(3)  # Wait for product page to load

# Find and click the CAD download button
try:
    cad_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "CadControl_downloadButton__38Gsb")))
    cad_button.click()
    print("Opened CAD download menu.")
except:
    print("CAD download button not found.")
    driver.quit()
    exit()

time.sleep(3)  # Allow time for modal to open

# Select the STEP file format (Modify if you need a different format)
try:
    step_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'STEP')]")))
    step_option.click()
    print("Selected STEP format.")
except:
    print("STEP format option not found.")
    driver.quit()
    exit()

time.sleep(5)  # Allow time for download

print(f"CAD file should be downloaded in: {download_path}")

# Close the browser
driver.quit()