# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-14 下午3:02 GMT+8

import json

mydict = {
    "store": {
        "book": [
            {"category": "reference",
             "author": "Nigel Rees",
             "title": "Sayings of the Century",
             "price": 8.95
             },
            {"category": "fiction",
             "author": "Evelyn Waugh",
             "title": "Sword of Honour",
             "price": 12.99
             },
        ],
    }
}


# python数据类型-->json字符串
json_str = json.dumps(mydict, ensure_ascii=False, indent=2)
print(json_str)

# json字符串-->python数据类型
json_dict = json.loads(json_str)
print(json_dict)

# json.dump() python数据类型-->写入 类文件对象
with open('mydict.json', 'w') as f:
    # f.write(json_str)
    json.dump(json_dict, f, ensure_ascii=False, indent=4)

# json.load() 类文件对象 读出 --> python数据类型
with open('mydict.json', 'r') as f:
    # old_ret = f.read()
    ret = json.load(f)
print(ret)


"""下面会报错!python规定Json字符串内部必须是双引号"""
a = "{'a':'n'}"
print(json.loads(a))