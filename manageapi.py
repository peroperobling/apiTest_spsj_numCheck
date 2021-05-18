# encoding: utf-8

import jsonpath
import requests
from RunMain import RunMain


class testApi(object):
    def __init__(self, method, url, data):
        self.method = method
        self.url = url
        self.data = data

    # @property
    def testApi(self):
        # 根据不同的访问方式来访问接口
        try:
            if self.method == 'post':
                if self.data == "":
                    print("No data post")
                # post方法还没写
                else:
                    # result = RunMain.send_post(self)
                    result = requests.post(self.url, data=(self.data).encode('utf-8'))
            elif self.method == 'get':
                if self.data == "":
                    result = RunMain().send_get(url=self.url,params='')
                else:
                    # result = RunMain().run_main('get',url=self.url,params=self.data)
                    # print('self.data:',self.data)
                    result = RunMain().send_get(url=self.url,params=self.data)
            # print('result:',result)
            # print('result.text:',result.text)
            return result
        except:
            print('失败')

    def getStatusCode(self):
        # 获取访问接口的状态码
        resp_stacode = self.testApi().status_code
        return resp_stacode

    def getJson(self):
        # 获取返回信息的json数据
        resp_json = self.testApi().json()
        return resp_json

    def getRespCode(self):
        resp_json = self.getJson()
        resp_code = jsonpath.jsonpath(resp_json, '$.code')[0]
        return resp_code

    def getText(self):
        # 获取返回信息的json数据
        resp_text = self.testApi().text
        return resp_text

if __name__ == '__main__':
    url_01 = 'http://192.168.1.20:8085/maintain/MacsHealthHistory/listDetail'  # 接口地址
    params_01 = {'serverId': '60000'}
    print(testApi('get',url_01,params_01))