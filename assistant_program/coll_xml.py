import os
import xml.dom.minidom


AnnoPath = './xmls/'
Annolist = os.listdir(AnnoPath)
rate = {} # 创建一个字典用于存放标签名和对应的出现次数
# total = 0
for annotation in Annolist:
    fullname = AnnoPath + annotation
    dom = xml.dom.minidom.parse(fullname) # 打开XML文件
    collection = dom.documentElement # 获取元素对象
    objectlist = collection.getElementsByTagName('object') # 获取标签名为object的信息
    for object in objectlist:
        namelist = object.getElementsByTagName('name') # 获取子标签name的信息
        objectname = namelist[0].childNodes[0].data # 取到name具体的值
        if objectname not in rate: # 判断字典里有没有标签，如无添加相应字段
            rate[objectname] = 0
        rate[objectname] += 1
        # total += 1

print(rate)

