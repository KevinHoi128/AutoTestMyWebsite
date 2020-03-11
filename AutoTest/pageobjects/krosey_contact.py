from framework.basepage import BasePage
from framework.logger import Logger

logger = Logger(logger = 'KroseyContact').getlog()
class KroseyContact(BasePage):

    input_box_name= "xpath=>//*[@id='wpcf7-f165-p343-o1']/form/p[1]/label/span/input"
    input_box_email= "xpath=>//*[@id='wpcf7-f165-p343-o1']/form/p[2]/label/span/input"
    input_box_comment= "xpath=>//*[@id='wpcf7-f165-p343-o1']/form/p[3]/label/span/textarea"
    submit_btn = "xpath=>//*[@id='wpcf7-f165-p343-o1']/form/p[4]/input"

    def type_name(self, text):
        self.type(self.input_box_name, text)
        logger.info('Input name.')

    def type_email(self, text):
        self.type(self.input_box_email, text)
        logger.info('Input email.')

    def type_comment(self, text):
        self.type(self.input_box_comment, text)
        logger.info('Input comment.')

    def send_submit_btn(self):
        self.click(self.submit_btn)
        logger.info('Submit.')
