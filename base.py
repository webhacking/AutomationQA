import unittest
from time import sleep
from selenium import webdriver

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class Base(unittest.TestCase):
    calendar_domain = 'https://calendar.google.com/'

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.start_client()
        self.driver.implicitly_wait(3)
        self.login()

    def tearDown(self):
        self.driver.close()

    def login(self):
        self.driver.get(self.calendar_domain)

        account = {
            'email' : '본인 이메일',
            'password' : '본인 패스워드'
        }

        for key, value in account.items():
            current_ele = self.driver.find_element_by_css_selector(f'input[type="{key}"][jsname="YPqjbf"]')
            current_ele.send_keys(value)

            next_button = self.driver.find_element_by_css_selector('content.CwaK9')
            next_button.click()

            sleep(1)

        try_count = 0
        while try_count < 10:
            try_count += 10 if self.driver.find_element_by_css_selector('body[jscontroller="phtQPb"]') else 1
            sleep(1)

