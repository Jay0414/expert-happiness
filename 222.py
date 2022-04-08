import requests
import json
设置URL
url = "https://kim-api1.kwaitalk.com/deploy/v2/notify/checkUpdate"
# 设置消息头
headers = {
    "x-auth-token":"09e49cb7ba3b851fdfa9d2d7961682a6",
    "Content-Type":"application/json"
    }
# 设置消息体
data = {
    "systemType":"ios",
    "deviceBrand":"apple",
    "curVersionStr":"2.6.20530",
    "deviceModel":"iPhone 12 Mini",
    "userId":"2ff21f2d301a401cb8138bb706e80c20",
    "deviceType":"ios",
    "deviceId":"65F4BD0A-350B-42B2-96BD-87FF374AA297",
    "netType":1,
    "powerRate":-100,
    "language":"zh",
    "systemVersion":"14.7.1",
    "curVersion":54167
}
# 获取相应
response=requests.post(url,headers=headers,data=json.dumps(data))
print("Status code:",response.status_code)
print(response.text)
# 解析相应
info=response.json()
# 验证数据
# assert str(info['answer'])=='reject'