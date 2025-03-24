from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

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

# Click on the first product link
product_links = driver.find_elements(By.CSS_SELECTOR, ".ListItem a")
if product_links:
    product_links[0].click()

time.sleep(3)

# Locate and click the CAD download button
try:
    cad_download_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Download CAD')]")
    cad_download_button.click()
    print("CAD download initiated.")
except:
    print("CAD download button not found.")
