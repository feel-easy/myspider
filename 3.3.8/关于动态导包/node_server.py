# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-1 下午5:00 GMT+8

import os
import time
import importlib

"""文件夹中新增的py文件,自动运行
# 定期 获取spiders中文件列表 和 上一次获取的列表做比对 对于新增的文件自动运行"""

class Node():
    old_file_list = []
    def get_file_list(self):
        file_list = os.listdir('./spiders')
        file_name_list = []
        for file in file_list:
            if file[0] != '_':
                file_name_list.append('spiders.' + file[:-3])
        return file_name_list

    def check_old_file_list(self):
        self.old_file_list = self.get_file_list()
        new_old = []
        for old in self.old_file_list:
            if old in self.get_file_list():
                new_old.append(old)
        return new_old

    def run(self):
        while 1:
            # 先执行新增文件
            now_list = self.get_file_list()
            new_list = list(set(now_list)-set(self.old_file_list))
            if new_list != []: print('发现新的可执行文件: {}'.format(new_list))
            for file in new_list:
                py_obj = importlib.import_module(file)
                func = getattr(py_obj, 'main')
                print('运行可执行文件: {}'.format(file+'.py'))
                func()
            # 检测移除的文件,同时清出旧文件列表
            self.old_file_list = self.check_old_file_list()

            # 将新增文件添加到oldfilelist
            self.old_file_list += new_list

            time.sleep(1)

            print(now_list, self.old_file_list, new_list)


if __name__ == '__main__':
    n = Node()
    n.run()
