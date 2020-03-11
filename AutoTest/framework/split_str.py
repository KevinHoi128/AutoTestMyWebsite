import time
from selenium import webdriver
from framework.basepage import BasePage

class GetSubString(object):

    def get_search_result(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(4)

        driver.get('https://www.baidu.com')
        driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        driver.find_element_by_id('su').click()
        time.sleep(1)
        search_result_string = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[2]/span').text
        print (search_result_string)

        new_string = search_result_string.split('约')[1]
        print(new_string)
        last_result = new_string.split('个')[0]
        print(last_result)
        driver.quit()

getstring = GetSubString()
getstring.get_search_result()