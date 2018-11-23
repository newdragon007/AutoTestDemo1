import requests

response=requests.get("https://www.baidu.com")
print(response.content)
if("baidu" in response.text):
    print("test pass")
