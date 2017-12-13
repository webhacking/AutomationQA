import unittest

from base import Base
from time import sleep


class Add(Base):
    def event(self, title):
        self.driver.get(self.calendar_domain)
        add_button = self.driver.find_element_by_css_selector('content > i.Gw6Zhc')
        add_button.click()

        sleep(1)

        title_field = self.driver.find_element_by_id('xTiIn')
        title_field.send_keys(title)

        apply_button = self.driver.find_element_by_id('xSaveBu')
        apply_button.click()

    def test_all(self):
        self.event(
            title='영어 공부 시작'
        )

unittest.main()
