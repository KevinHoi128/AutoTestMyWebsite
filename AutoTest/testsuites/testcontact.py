# coding=utf-8
import time
import unittest
from framework.basepage import BasePage
from framework.browser_engine import BrowserEngine
from pageobjects.krosey_contact import KroseyContact
from framework.logger import Logger

logger = Logger(logger = 'ContactKrosey').getlog()
class ContactKrosey(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        bse = BrowserEngine(cls)
        cls.driver = bse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def testcontact(self):
        kroseycontact = KroseyContact(self.driver)
        self.driver.find_element_by_xpath("//*[@id='menu-item-395']/a/span").click()
        logger.info('Click to contact page.')

        kroseycontact.type_name('Kevin')
        time.sleep(1)
        kroseycontact.type_email('krose.kachon@gmail.com')
        time.sleep(1)
        kroseycontact.type_comment('Blablabla.')
        time.sleep(1)
        kroseycontact.get_windows_img()
        time.sleep(1)
        kroseycontact.send_submit_btn()
        time.sleep(2)
        kroseycontact.get_windows_img()
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()
