# -*- coding:utf-8 -*- 
"""
describe：读取yaml文件
Author：tang
Email：tallyx@163.com
Time: 2023/4/17 
Software: PyCharm
"""

import yaml, os
from Config.Config import Config


class ReadYaml(object):

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(file=self.filename, mode="r", encoding='utf8', ) as f:
            data = f.read()
        data_yaml = yaml.load(data, Loader=yaml.FullLoader)
        for value in data_yaml:
            value["url地址"] = Config.url + value["url地址"]
        return data_yaml


if __name__ == '__main__':
    y = ReadYaml(r"E:\playwright-demo\TestDatas\TestLoginData.yaml").read()
    print(y)
