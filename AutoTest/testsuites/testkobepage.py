# coding=utf-8
import time
import unittest
from framework.basepage import BasePage
from framework.browser_engine import BrowserEngine
from pageobjects.krosey_homepage import RoseHomePage
from pageobjects.krosey_practicepage import PracticeRosePage
from pageobjects.krosey_kobepage import KobePage
from framework.logger import Logger

logger = Logger(logger = 'ToKobePage').getlog()
class FuncAndKobePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        bse = BrowserEngine(cls)
        cls.driver = bse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_to_kobe_page(self):
        rosehomepage = RoseHomePage(self.driver)
        self.driver.find_element_by_xpath("//*[@id='menu-item-518']/a/span").click()
        logger.info("Click to practice page.")
        rosehomepage.get_windows_img()
        time.sleep(1)

        practicerosepage = PracticeRosePage(self.driver)
        self.driver.find_element_by_xpath("//*[@id='elementor-tab-title-1272']/a").click()
        logger.info("Switch to webpage folder.")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='elementor-tab-content-1272']/ol/li[1]/span/a").click()
        logger.info("Click to Kobe page.")
        time.sleep(1)
        practicerosepage.get_windows_img()
        time.sleep(1)

        kobepage = KobePage(self.driver)
        self.driver.find_element_by_xpath("//*[@id='kobe']/div[3]/div/div/div/div/div[3]/div/div/a/span/span").click()
        logger.info("Click to kobe tribute video.")
        kobepage.get_windows_img()
        self.driver.back()
        self.driver.find_element_by_xpath("//*[@id='scroll_here1']/div/div/div/div/div/div[3]/div/div/a/i").click()
        logger.info("Click to kobe block2.")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='scroll_here1']/div/div/div/div/div/div[4]/div/div/a/i").click()
        logger.info("Click to kobe block3.")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='scroll_here1']/div/div/div/div/div/div[2]/div/div/a/i").click()
        logger.info("Click to kobe block4.")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='scroll_here3']/div/div/div/div/div/div[2]/div/div/a/i").click()
        logger.info("Click to kobe block5.")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='scroll_here4']/div/div/div/div/div/div[2]/div/div/a/i").click()
        logger.info("Click to final kobe block.")
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()
