# -*- coding:utf-8 -*-
import configparser
import os.path
from framework.logger import Logger
from selenium import webdriver

logger = Logger(logger = 'BrowserEngine').getlog()

class BrowserEngine(object):

    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/AutoTest/tools/chromedriver.exe'
    ie_driver_path = dir + '/AutoTest/tools/IEDriverServer.exe'

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/AutoTest/Config/config.ini'
        config.read(file_path)

        browser = config.get("browserType", "browserName")
        logger.info('You had select %s browser.' % browser)
        url = config.get("testServer", "URL")
        logger.info('The test server url is: %s' % url)

        if browser == 'FireFox':
            driver = webdriver.Firefox()
            logger.info('Starting firefox browser.')
        elif browser == 'Chrome':
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info('Starting Chrome browser.')
        elif browser == 'IE':
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info('Starting IE browser.')

        driver.get(url)
        logger.info('Open url: %s' % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(2)
        logger.info("Set implicitly wait 2 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()
