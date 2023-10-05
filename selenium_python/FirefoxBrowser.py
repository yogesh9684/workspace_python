
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FFService


Firefoxservice = FFService(executable_path="C:\\browser_drivers\\geckodriver.exe")
driver = webdriver.Firefox(service=Firefoxservice)
driver.get("https://swayogsoftware.com/")




