import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


os.system("cls")

driver = webdriver.Chrome()
url = "https://www.nseindia.com/get-quotes/equity?symbol=sbi"
driver.get(url)

try:
    menu = driver.find_element(By.CLASS_NAME, "nav-item")
    hidden_submenu = driver.find_element(By.CLASS_NAME, "nav-link")

    ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

    historical_data_link = driver.find_element(By.XPATH, "//a[contains(@href,'/reports-indices-historical-vix')]")
    historical_data_link.click()

    one_year_link = driver.find_element_by_id('oneY')
    one_year_link.click()

    download_link = driver.find_element_by_id('dwldcsv')
    download_link.click()

except Exception as ex:
    print("***********Exception Message**************")
    print(ex)
    print("***********Exception Message**************")

driver.quit()
