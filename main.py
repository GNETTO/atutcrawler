# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import wget
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

search_input = "abidjan+dominique"
#time.sleep(5)
#search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.CSS_SELECTOR("input[name='q']")))
search = driver.find_element(By.NAME, 'q')
print(search.text)
search.send_keys(search_input)
time.sleep(2)
search.send_keys(Keys.RETURN)

time.sleep(2)
search_data = driver.find_element(By.ID, 'search')
time.sleep(2)
print(search_data.text)
search_data = driver.find_element(By.ID, 'pnnext')


#driver.quit()
#driver.fin
def print_hi(name):
    print("slist")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
