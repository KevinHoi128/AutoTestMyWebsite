import configparser
import os

class TestReadConfigFile(object):

    def get_value(self):
        root_dir = os.path.dirname(os.path.abspath('.'))
        print (root_dir)

        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/Config/config.ini'
        config.read(file_path)

        browser = config.get('browserType', 'browserName')
        url = config.get("testServer", "URL")

        return(browser, url)

trcf = TestReadConfigFile()
print (trcf.get_value())
