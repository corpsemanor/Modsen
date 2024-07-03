from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com")

driver.add_cookie({"name": "key", "value": "value"})

cookie_value = driver.get_cookie("key")
print(f"Cookie Value: {cookie_value}")

driver.delete_cookie("key")

cookie_value_deleted = driver.get_cookie("key")
print(f"Cookie Value After Deletion: {cookie_value_deleted}")

driver.quit()