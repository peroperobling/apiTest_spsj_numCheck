# encoding: utf-8

import unittest
from testApi import TestRunSpsj
from HTMLTestRunner import HTMLTestRunner

testunit = unittest.TestSuite()
testunit.addTest(unittest.makeSuite(TestRunSpsj))
# testunit.addTest(TestRunPrometheus("test_01_1"))
# testunit.addTest(TestRunPrometheus("test_01_2"))
fp = open('./result.html','wb')
runner = HTMLTestRunner(stream=fp,title="API测试报告",description="测试执行情况")
runner.run(testunit)
fp.close()