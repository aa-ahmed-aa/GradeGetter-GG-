# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, sys


class Test1(unittest.TestCase):
    student_id=""
    password=""

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "http://misdb.minia.edu.eg/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_1(self):
        driver = self.driver
        driver.get(self.base_url + "/pub/stud.aspx") 
        driver.find_element_by_id("txt_code").clear()
        driver.find_element_by_id("txt_code").send_keys(Test1.student_id)
        driver.find_element_by_id("txt_pass").clear()
        driver.find_element_by_id("txt_pass").send_keys(Test1.password)
        driver.find_element_by_id("Button1").click()
        time.sleep(9000)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


def main():
    with open('data.txt','r') as file:
        data = []
        for line in file:
            data.append(line.strip('\n'))


        Test1.student_id = data[0]
        Test1.password = data[1]
         
    unittest.main()



if __name__ == "__main__":
    main()
