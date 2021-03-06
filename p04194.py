'''
分析百度词典
打开f12
输入girl
每次输入一个字母都有请求
请求地址：http://fanyi.baidu.com/sug
利用network 发现 FormData的值是 kw：girl
json格式  需要用到json包
'''
from urllib import  request,parse
import json

'''
大致流程：
利用data构造的内容，然后URLopen打开
返回一个json格式的结果
结果就是应该是girl的释义
'''

baseurl = 'http://fanyi.baidu.com/sug'
#存放用来模拟form的数据一定是dict格式
data = {
    #girl 是翻译输入的英文内容，应该是由用户输入，此处使用硬编码
    'kw':'girl'
}
#需要用parse模块进行编码
data = parse.urlencode(data).encode("utf-8")
#构造一个请求头，请求头至少包括传入的数据长度
#request要求传入的请求头是一个dict格式
headers ={
    #因为使用post请求，至少应该包含content-length 字段
    'Content-Length':len(data)

}
#有了headers，data，url 就可以尝试发出请求了
rsp = request.urlopen(baseurl,data=data)
json_data = rsp.read().decode()
print(json_data)
#把json字符串转化为字典
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

for item in json_data['data']:
    print(item['v'],"--",item['v'])