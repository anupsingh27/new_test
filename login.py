from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

def login_func():
    driver=webdriver.Firefox()
    #print driver
    driver.get("https://betassltest.ajayvision.com/home")
    ele=driver.find_element_by_link_text("LOGIN")
    ele.click()
    passw="anupsingh001"
    mail="anup.singh@visionias.in"

    e1=driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/input')
    e2=driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/div[2]/div/div/div/form/div[2]/div/input')
    #clear the input fields
    e1.clear()
    e2.clear()
    #entering data into login fields
    e1.send_keys(mail)
    e2.send_keys(passw)
    #locating login button and clicking
    btn=driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/div[2]/div/div/div/form/div[5]/button')
    btn.click()
    #driver.quit()
    #time.sleep(10)
    driver.implicitly_wait(30)
    #classroom = driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[4]/a')
    #driver.implicitly_wait(5)
    #classroom.click()
    test_series = driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[3]/div/a').click()
    prelims=driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[3]/div/div/a[1]')
    prelims.click()

    driver.implicitly_wait(30)

    target_yr_select = Select(driver.find_element_by_xpath('//*[@id="year"]'))
    select=target_yr_select.select_by_value('2020')

    driver.implicitly_wait(10)

    language_select = Select(driver.find_element_by_xpath('//*[@id="medium"]'))
    select=language_select.select_by_value('English')

    driver.implicitly_wait(10)

    subject_select = Select(driver.find_element_by_xpath('//*[@id="subject"]'))
    select=subject_select.select_by_value('General Studies')
    driver.implicitly_wait(10)

    search=driver.find_element_by_xpath('/html/body/div[1]/div[10]/div/center/button')
    driver.implicitly_wait(10)
    search.click()
    #select=driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul/li/div/a')
    #select.click()
    #logout=driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul/li/div/div/a[6]')
    #logout.click()

if __name__=="__main__":
    login_func()

"""elect=driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul/li/div/a')
select.click()
logout=driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul/li/div/div/a[6]')
logout.click()"""

