from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def wait_css(driver,css_doubleCode):
  return WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR,css_doubleCode)))
def wait_xpath(driver, xpath_simpleCode):
   return WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, xpath_simpleCode)))
