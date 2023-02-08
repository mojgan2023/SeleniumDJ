from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

"""
Test Website Digikala
"""

# open browser (by chrome driver) and open digikala.com
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.digikala.com/')
sleep(5)

# find the login link and click on it
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/header/div[2]/div/div/div[2]/a/div[2]').click()
sleep(2)

# find the username input and add data on it
username = '09226330757'
driver.find_element(By.NAME, 'username').send_keys(username)
sleep(2)

# click on login button for continue
driver.find_element(By.XPATH ,'/html/body/div[1]/main/div[2]/div[2]/form/button/div[2]').click()
sleep(2)

# find the password input and add data on it
password = 'Deu@2022'
driver.find_element(By.NAME, 'password').send_keys(password)
sleep(2)

# click on continue button for login
driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/button[3]/div[2]').click()
sleep(2)

# click on account button for check the username
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/header/div[2]/div/div/div[2]/div[1]/div[1]').click()
sleep(10)

# close the browser
driver.quit()