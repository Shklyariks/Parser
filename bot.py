from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


url = 'https://web.telegram.org/z/'

s = Service('/Users/sergejsklarik/PycharmProjects/Parserproject/chrome/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
driver = webdriver.Chrome(service=s, options=options)

try:
   driver.get(url=url)
   time.sleep(20)
   # email_adress = email
   # password = password
   #
   # email_input = driver.find_element(By.ID, 'identifierId')
   # email_input.clear()
   # email_input.send_keys(email_adress)
   # time.sleep(3)
   #
   # buttom_next = driver.find_element(By.ID, 'identifierNext').click()
   # time.sleep(20)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

