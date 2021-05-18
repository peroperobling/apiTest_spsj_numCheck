# encoding: utf-8

import jsonpath
import requests

# from Excel.globals import CASE

session = requests.session()

class RunMain:

    def send_get(self,url,params):
        """
        查询每个磁盘的使用情况(B)=>G
        :return:
        """
        login()
        headers = {
            'Authorization': 'Bearer ' + token
        }
        # params = {
        #     'instance': '192.168.1.20',
        #     'time': '2021-03-30 12:00:00'
        # }
        resp = session.request(url=url, method='get', params=params, headers=headers)
        return resp

    def send_post(self):
        login()
        pass

    # def run_main(self,method,url=None,params=None):
    #     result = None
    #     # login()				# 【【重点】】
    #     if method == 'post':
    #         result = self.send_post()
    #     elif method =='get':
    #         result = self.send_get(url,params)
    #     else:
    #         print("错误")
    #     return result


def login():
        """
        登录
        :return:
        """
        global token
        url = 'http://192.168.1.20:80/api/login'
        params = {
            "username": "superadmin",
            "password": "abcd=1234"
        }
        resp = session.request(url=url, method='get', params=params)
        resp_json = resp.json()
        # 使用jsonpath从响应结果中提取token字段
        token = jsonpath.jsonpath(resp_json, '$.token')[0]
        # print('token:',token)


if __name__ == '__main__':
    url_01 = 'http://192.168.1.20:8080/api/rawNetFlow/getClientRawFlowTrend'  # 接口地址
    params_01 ={'srcIp':'192.168.1.20'}
    # resp = RunMain().run_main('get',url_01,params_01)		# 【【重点】】
    # print(type(resp))
    # stac = resp.status_code
    # print(stac)
    # # print('resp:',resp)
    # print(resp.json())

    # for i in range(0, 1):
    #     # api = testApi(CASE.method[i], CASE.url[i], CASE.data[i])
    #     # resp = RunMain().run_main('get',url_01,CASE.data[i])		# 【【重点】】
    #     resp = RunMain().run_main('get','http://192.168.1.20:8085/maintain/MacsHealthHistory/listDetail',json.loads(CASE.data[i]))		# 【【重点】】
    #     print(CASE.data[i])
    #     print('q:',CASE.data[i])
    #     print(resp)
    #     print(resp.json())

    result = RunMain().send_get(url_01,'')
    print(result)
