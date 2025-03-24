from selenium import webdriver
import pickle
import time

options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir=C:\\Users\\samatya\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("--profile-directory=Default")  # Or your actual profile
options.add_argument("--disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.89 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.get("https://www.mcmaster.com/")

# Wait for manual login
input("Log in manually and press ENTER to save cookies...")

# Save cookies
pickle.dump(driver.get_cookies(), open("mcmaster_cookies.pkl", "wb"))
print("Cookies saved!")

driver.quit()
