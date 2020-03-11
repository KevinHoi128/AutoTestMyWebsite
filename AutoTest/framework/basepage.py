import os.path
import time
from selenium.common.exceptions import NoSuchElementException
from framework.logger import Logger

logger = Logger(logger = 'BasePage').getlog()
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def back(self):
        self.driver.back()
        logger.info('Click back on current page.')

    def forward(self):
        self.driver.forward()
        logger.info('Click forward on current page.')

    """
    def open_url(self, url):
        self.driver.get(url)
    """

    """
    def take_screenshot(self):

        file_path = os.path.dirname(os.getcwd()) + '/Screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'

        try:
            self.driver.get_screenshot_as_file(screen_name)
            mylogger.info('Take a screenshot and save')

        except Exception as e:
            mylogger.info('Screenshot error ')
            mylogger.error('Screenshot error ', format(e))
    """

    def quit_browser(self):
        self.driver.quit()

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info('Wait for %d seconds.' % seconds)

    def close(self):
        try:
            self.driver.close()
            logger.info('Closing and quit the browser.')
        except NameError as e:
            logger.error('Failed to quit the browser with %s' % e)

    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/AutoTest/Screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('Had take screenshot and save to folder : /Screenshots')
        except NameError as e:
            logger.error('Failed to take screenshot! %s' % e)
            self.get_windows_img()

    def find_element(self, selector):
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == 'i' or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element \' %s \' successful by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element \' %s \' successful by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error('NoSuchElementException: %s' % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")
 
        return element

    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \'%s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    def click(self, selector):

        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element \'%s \' was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)
