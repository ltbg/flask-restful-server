# --*-- coding=utf-8 --*--
import urllib2
import urllib
import json
weatherHtml = urllib.urlopen('http://localhost:5000/todos/ip1')
#通过urllib模块中的urlopen的方法打开url
weatherHtml1 = weatherHtml.read()
#通过read方法获取返回数据
print (weatherHtml1)
#打印返回信息
weatherJSON = json.loads(weatherHtml1)
# #将返回的json格式的数据转化为python对象，json数据转化成了python中的字典，按照字典方法读取数据
print "python的字典数据：",weatherJSON
print "字典中的task数据",weatherJSON["task"]
x=weatherJSON["task"]
print(x)
# ********************************************************************************************
# 以下步骤为客户端连接数据存储服务器
# x=weatherJSON["task"]
# nextserver=urllib.urlopen('http://localhost:5000/saveserver/x')
