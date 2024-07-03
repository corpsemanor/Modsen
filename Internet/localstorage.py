from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com")

driver.execute_script("window.localStorage.setItem('key', 'value');")

local_storage_value = driver.execute_script("return window.localStorage.getItem('key');")
print(f"LocalStorage Value: {local_storage_value}")

driver.execute_script("window.localStorage.removeItem('key');")

local_storage_value_deleted = driver.execute_script("return window.localStorage.getItem('key');")
print(f"LocalStorage Value After Deletion: {local_storage_value_deleted}")

driver.quit()