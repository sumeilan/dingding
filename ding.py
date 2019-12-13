#-*- coding:utf-8 -*-
import requests
import json

def dingmessage():
# 请求的URL，WebHook地址
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=433a9ca07bc46a33373b746049f4a621111fd95021a2c5f3081d3f0de35eb043"
#构建请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
}
#构建请求数据
    tex = "demo包更新啦，下载地址：https://fir.im/ux5a"
    message ={
        "msgtype": "text",
        "text": {
            "content": tex
        },
        "at": {

            "isAtAll": False
        }

    }
#对请求的数据进行json封装
    message_json = json.dumps(message)
#发送请求
    info = requests.post(url=webhook,data=message_json,headers=header)
#打印返回的结果
    print(info.text)

if __name__=="__main__":
    dingmessage()