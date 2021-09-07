import os
from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.keys import Keys
import time

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Messenger():
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = '127.0.0.1:62025'
        desired_caps['newCommandTimeout'] = '60*60'
        desired_caps['noReset'] = 'True'
        desired_caps['appPackage'] = 'com.facebook.mlite'
        desired_caps['appActivity'] = 'com.facebook.mlite.coreui.view.MainActivity'

        self.driver = webdriver.Remote('http://127.0.0.2:4743/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self,number):
        dist={}

        contacts = self.driver.find_element_by_accessibility_id("Contacts Tab")
        contacts.click()

        text_field = self.driver.find_element_by_id("com.facebook.mlite:id/edit_text_search")
        text_field.send_keys(number)   

        el3 = self.driver.find_element_by_accessibility_id("Search")
        el3.click() 

        try:
            name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.facebook.mlite:id/name")))
            name.click()

            textView = self.driver.find_elements_by_class_name("android.widget.TextView")
            name = textView[0].text
            dist["Name"] = name

            options = self.driver.find_element_by_accessibility_id("More options")
            options.click()
            
            option_textView = self.driver.find_elements_by_class_name("android.widget.TextView")
            option_textView[0].click()
            
            find_url = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "com.android.chrome:id/url_bar")))
            time.sleep(1)
            profile_link = find_url.text

            dist["Profile_link"]=profile_link
            return {"data":[dist]}

        except Exception:
            print("[-]  No user found !!")
            dist["Name"] = ""
            dist["Profile_link"] = ""
            return {"data":[dist]}


