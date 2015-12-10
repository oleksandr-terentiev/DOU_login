__author__ = 'ali'
# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchElementException
import time, re
from appium import webdriver
from selenium.webdriver import DesiredCapabilities
import json


class Dou:
    def __init__(self, brwsr):
        json_t = json.load(open("browsers.json"))
        self.cap = DesiredCapabilities.__dict__[brwsr]
        self.cap.update(json_t[brwsr]["caps"])
        self.base_url = json_t[brwsr]["url"]
        self.driver = webdriver.Remote(json_t[brwsr]["server"], self.cap)
        self.driver.implicitly_wait(30)

    def login(self, login, pswd):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("login-link").click()
        self.driver.find_element_by_id("_loginByMail").click()
        self.driver.find_element_by_name("username").clear()
        self.driver.find_element_by_name("username").send_keys(login)
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(pswd)
        time.sleep(3)
        self.driver.find_element_by_css_selector("button.big-button.btnSubmit").click()

    def am_i_logged(self):
        try:
            time.sleep(5)
            self.driver.find_element_by_css_selector("img.g-avatar[alt='Alex Job']").click()
            self.driver.find_element_by_link_text("Alex Job")
        except NoSuchElementException:
            self.driver.quit()
            return False
        else:
            return True

    def close_brwsr(self):
        self.driver.quit()

    def login_ban(self):
        time.sleep(0.30)
        try:
            self.driver.find_element_by_id("wrong-password-message")
        except NoSuchElementException:
            self.driver.quit()
            return False
        else:
            return self.driver.find_element_by_id("wrong-password-message").is_displayed()
