from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def browser(): 
    #making instance of firefox browser
    driver = webdriver.Firefox()
    print driver
    return 2
    #navigating to home page
    #driver.get("https://betassltest.ajayvision.com/home")
    """
    #wating until login button is not loaded or max of 5 sec
    try:
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="log-in"]')))
    except Exception as e:
        print "Error : "+str(e)"""
