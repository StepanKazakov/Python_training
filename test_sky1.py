# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSky11():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_sky11(self):
    # Test name: sky1_1
    # Step # | name | target | value
    # 1 | open | /login?redirect=http://teachers.skyeng.ru | 
    self.driver.get("https://id.skyeng.ru/login?redirect=http://teachers.skyeng.ru")
    # 2 | setWindowSize | 1559x921 | 
    self.driver.set_window_size(1559, 921)
    # 3 | click | css=tcc-calendar-event:nth-child(94) .box-hover | 
    self.driver.find_element(By.CSS_SELECTOR, "tcc-calendar-event:nth-child(94) .box-hover").click()
    # 4 | click | css=.flex-grow:nth-child(3) .text-center | 
    self.driver.find_element(By.CSS_SELECTOR, ".flex-grow:nth-child(3) .text-center").click()
    # 5 | click | css=.ng-invalid:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".ng-invalid:nth-child(2)").click()
    # 6 | type | css=.ng-dirty:nth-child(2) | new event
    self.driver.find_element(By.CSS_SELECTOR, ".ng-dirty:nth-child(2)").send_keys("new event")
    # 7 | click | css=.class-date | 
    self.driver.find_element(By.CSS_SELECTOR, ".class-date").click()
    # 8 | select | css=.class-date | label=Четверг, 15 декабря
    dropdown = self.driver.find_element(By.CSS_SELECTOR, ".class-date")
    dropdown.find_element(By.XPATH, "//option[. = 'Четверг, 15 декабря']").click()
    # 9 | click | css=.class-date > .ng-star-inserted:nth-child(46) | 
    self.driver.find_element(By.CSS_SELECTOR, ".class-date > .ng-star-inserted:nth-child(46)").click()
    # 10 | click | css=.cursor-pointer:nth-child(3) .color-circle__right | 
    self.driver.find_element(By.CSS_SELECTOR, ".cursor-pointer:nth-child(3) .color-circle__right").click()
    # 11 | click | css=.-type-primary > .text-container | 
    self.driver.find_element(By.CSS_SELECTOR, ".-type-primary > .text-container").click()
    # 12 | click | css=.fa-chevron-right > path | 
    self.driver.find_element(By.CSS_SELECTOR, ".fa-chevron-right > path").click()
    # 13 | click | css=.fa-chevron-right > path | 
    self.driver.find_element(By.CSS_SELECTOR, ".fa-chevron-right > path").click()
    # 14 | click | css=.fa-chevron-right > path | 
    self.driver.find_element(By.CSS_SELECTOR, ".fa-chevron-right > path").click()
    # 15 | click | css=.fa-chevron-right > path | 
    self.driver.find_element(By.CSS_SELECTOR, ".fa-chevron-right > path").click()
    # 16 | click | css=.fa-chevron-right > path | 
    self.driver.find_element(By.CSS_SELECTOR, ".fa-chevron-right > path").click()
    # 17 | click | css=.fa-chevron-right > path | 
    self.driver.find_element(By.CSS_SELECTOR, ".fa-chevron-right > path").click()
    # 18 | click | css=.ng-star-inserted:nth-child(26) .long-view__title | 
    self.driver.find_element(By.CSS_SELECTOR, ".ng-star-inserted:nth-child(26) .long-view__title").click()
    # 19 | click | css=.-type-secondary > .text-container | 
    self.driver.find_element(By.CSS_SELECTOR, ".-type-secondary > .text-container").click()
    # 20 | close |  | 
    self.driver.close()
  
