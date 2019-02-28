# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-23 下午3:25 GMT+8

from pymongo import MongoClient

"""无需权限认证"""
# client = MongoClient() # 实例化一个连接对象
#
# # 创建集合操作对象 col = client.数据库名.集合名
# col = client.test14.heihei
#
# ret = col.insert({'a':'pa'})
# print(ret)

"""权限认证"""
uri = 'mongodb://%s:%s@127.0.0.1'% ('python', 'python')
# uri = 'mongodb://账号:密码@目标服务器的ip'
# 实例化一个连接对象
client = MongoClient(uri, port=27017)
# 创建集合操作对象 col = client.数据库名.集合名
col = client.test14.heihei

"""插入数据"""
# ret = col.insert({'pa':'a'})
# print(ret) # _id中Object对象中的内容

# item_list = [{'pa':i} for i in range(5)]
# rets = col.insert(item_list)
# for ret in rets:
#     print(ret)

"""查找"""
# ret = col.find_one({'pa': 'a'})
# print(ret)
# import json
# # _ = ret.pop('_id')
# del ret['_id']
# print(json.dumps(ret))

# # find()找多条,返回的是一个cursor游标对象,只能遍历一次
# rets = col.find()
# # a = []
# for ret in rets:
#     print(ret)
#     # a.append(ret)
# print('='*10)
# for ret in rets:
#     print(ret)

"""更新"""
# ret = col.update({},
#                  {'$set':{'b':'haha'}})
# ret = col.update({},
#                  {'$set':{'a':'xxx'}},
#                  multi=True, # multi=True更新多条
#                  upsert=True) # upsert=True存在就更新,不存在就插入

"""删除"""
# ret = col.delete_one({'pa':'a'})
# print(ret)
# ret = col.delete_many({'a':'xxx'})
# print(ret)

