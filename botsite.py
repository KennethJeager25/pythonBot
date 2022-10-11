from selenium import webdriver
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

navegador = './chromedriver.exe'
url='https://mypid.smartpid.com/mypid/'


driver = webdriver.Chrome(navegador)
driver.get(url)

driver.find_element_by_xpath('//*[@id="sign-in-container"]/ion-grid/ion-row[1]/ion-col/ion-list/ion-item[1]/ion-input/input').send_keys('marrito@me.com')
driver.find_element_by_xpath('//*[@id="sign-in-container"]/ion-grid/ion-row[1]/ion-col/ion-list/ion-item[2]/ion-input/input').send_keys('goodbeer#2022')
driver.find_element_by_xpath('//*[@id="sign-in-container"]/ion-grid/ion-row[2]/ion-col/ion-button').click()


url='https://mypid.smartpid.com/mypid/dashboard'
driver.refresh()

driver.execute_script("window.localStorage.setItem('EMAIL', 'marrito@me.com')")
driver.execute_script("window.sessionStorage.setItem('MY_PASSWORD', 'goodbeer#2022')")
driver.execute_script("window.sessionStorage.setItem('MY_SESSION', 'ALREADY_PRESENT')")
driver.get(url)

time.sleep(3)

driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-dashboard/ion-content/ion-grid/ion-row/ion-col[3]/ion-card/div[1]/ion-item-divider/div/div/ion-segment/ion-segment-button[2]').click()
