from framework.basepage import BasePage

class KobePage(BasePage):

    next_photo1 = "xpath=>//*[@id='scroll_here1']/div/div/div/div/div/div[3]/div/div/a/i"
    next_photo2 = "xpath=>//*[@id='scroll_here1']/div/div/div/div/div/div[4]/div/div/a/i"
    next_photo3 = "xpath=>//*[@id='scroll_here1']/div/div/div/div/div/div[2]/div/div/a/i"
    next_photo4 = "xpath=>//*[@id='scroll_here3']/div/div/div/div/div/div[2]/div/div/a/i"
    next_photo5 = "xpath=>//*[@id='scroll_here4']/div/div/div/div/div/div[2]/div/div/a/i"
    kobe_link = "xpath=>//*[@id='kobe']/div[3]/div/div/div/div/div[3]/div/div/a/span/span"

    def click_kobe_link(self):
        self.click(self.kobe_link)
        self.sleep(2)

    def click_next_photo1(self):
        self.click(self.next_photo1)
        self.sleep(1)

    def click_next_photo2(self):
        self.click(self.next_photo2)
        self.sleep(1)

    def click_next_photo3(self):
        self.click(self.next_photo3)
        self.sleep(1)

    def click_next_photo4(self):
        self.click(self.next_photo4)
        self.sleep(1)

    def click_next_photo5(self):
        self.click(self.next_photo5)
        self.sleep(1)
