# coding=utf-8
import unittest
import os
import HTMLTestRunner
import time

#文件儲存路徑
report_path = os.path.dirname(os.path.abspath('.')) + '/AutoTest/test_report/'
#系統時間
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

#文件名稱格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile, "wb")

suite = unittest.TestLoader().discover("testsuites")

if __name__ == '__main__':
    runner=HTMLTestRunner.HTMLTestRunner(fp, title=u"KroseY網站測試報告", description=u"用例測試情況")
    runner.run(suite)
