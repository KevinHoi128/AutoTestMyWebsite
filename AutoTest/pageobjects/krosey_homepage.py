from framework.basepage import BasePage

class RoseHomePage(BasePage):

    practice_link = "xpath=>//*[@id='menu-item-518']/a/span"

    def click_practice(self):
        self.click(self.practice_link)
        self.sleep(2)