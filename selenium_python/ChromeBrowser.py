import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service


chrome_service = Service(executable_path="C:\\browser_drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
driver.maximize_window()
driver.get("https://swayogsoftware.com/")
time.sleep(20)

