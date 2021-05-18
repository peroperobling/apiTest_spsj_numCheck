# encoding: utf-8

import json
import unittest

import ddt as ddt

from manage import readExcel
from manageapi import testApi

# host = "http://192.168.1.20:"

file_path = "TestCase.xlsx"
testdata = readExcel(file_path).excel_table(0)
testdata_1 = readExcel(file_path).excel_table(1)
testdata_2 = readExcel(file_path).excel_table(2)
# print(testdata)

@ddt.ddt
class TestRunSpsj(unittest.TestCase):
    # def setUp(self):
    #     # self.run_main1 = RunMain()
    #     print('开始测试……')

    # 测试用例必须以test开头
    @ddt.data(*testdata)
    def test_01(self, data):
        # print('用例名称：', data['Number'])
        # print('用例名称：', data['Name'])
        # print('用例名称：', data['Method'])
        # print('用例名称：', data['Url'])
        # print('用例名称：', data['Data'])
        # print('用例名称：', data['Status_code'])

        # 访问接口
        print("测试模块：首页摄像头访问率/访问率报表")
        if data['Data'] == "":
            api = testApi(data['Method'], data['Url'], data['Data'])
        else:
            api = testApi(data['Method'], data['Url'], json.loads(data['Data']))

        # 断言
        apitext = api.getText()
        apicode = api.getRespCode()

        if apitext==data['Expected_result']:
            # print('{}、{}:测试成功。json数据为:{}'.format(data['Number'], data['Name'], apijson))
            print('{}:测试成功。json数据为:{}'.format(data['Name'], apitext))
        else:
            # print('{}、{}:测试失败'.format(data['Number'], data['Name']))
            print('{}:测试失败。json数据为:{}'.format(data['Name'], apitext))
        self.assertEqual(data['code'], apicode, 'code错误')
        self.assertEqual(data['Expected_result'], apitext, '响应内容不一致')

    @ddt.data(*testdata_1)
    def test_02(self, data):
        print("测试模块：终端访问")

        if data['Data'] == "":
            api = testApi(data['Method'], data['Url'], data['Data'])
        else:
            api = testApi(data['Method'], data['Url'], json.loads(data['Data']))
        apitext = api.getText()
        apicode = api.getRespCode()

        if apitext == data['Expected_result']:
            print('{}:测试成功。json数据为:{}'.format(data['Name'], apitext))
        else:
            print('{}:测试失败。json数据为:{}'.format(data['Name'], apitext))
        self.assertEqual(data['code'], apicode, 'code错误')
        self.assertEqual(data['Expected_result'], apitext, '响应内容不一致')

    @ddt.data(*testdata_2)
    def test_03(self, data):
        print("测试模块：摄像头被访问")

        if data['Data'] == "":
            api = testApi(data['Method'], data['Url'], data['Data'])
        else:
            api = testApi(data['Method'], data['Url'], json.loads(data['Data']))
        apitext = api.getText()
        apicode = api.getRespCode()

        if apitext == data['Expected_result']:
            print('{}:测试成功。json数据为:{}'.format(data['Name'], apitext))
        else:
            print('{}:测试失败。json数据为:{}'.format(data['Name'], apitext))
        self.assertEqual(data['code'], apicode, 'code错误')
        self.assertEqual(data['Expected_result'], apitext, '响应内容不一致')


if __name__ == '__main__':

    unittest.main(verbosity=2)