from framework.basepage import BasePage

class PracticeRosePage(BasePage):

    webpage_folder = "xpath=>//*[@id='elementor-tab-title-1272']/a"
    kobe_page = "xpath=>//*[@id='elementor-tab-content-1272']/ol/li[1]/span/a"

    def switch_webpage_folder(self):
        self.click(self.webpage_folder)
        self.sleep(2)

    def click_kobe_page(self):
        self.click(self.kobe_page)
        self.sleep(2)
