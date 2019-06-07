from login import login

login_func()

"""
try:
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="log-in"]')))
except Exception as e:
    print "Error : "+str(e)
"""
test_series = select=driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[3]/div/a')
test_series.click()
prelims=driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[3]/div/div/a[1]')
prelims.click()
#select=driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul/li/div/a')
select.click()
logout=driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul/li/div/div/a[6]')
logout.click()
