# -*- coding:utf-8 -*- 
"""
describe：设置全局环境变量
Author：tang
Email：tangllyx@163.com
Time: 2023/4/19 
"""
import random, time, re


class BuildInLibrary():
    glob_parameter = {}  # 存全局变量

    def set_glob_parameter(self, key, value):
        """把value的值放入变量名 key 中，"""
        # 1.提取 key   ##{{first_phone}}
        parameter_key = re.fullmatch(r'{{(\w+)}}', key).group(1)
        # 2.保存参数
        self.glob_parameter[parameter_key] = value
        return self.glob_parameter.get(parameter_key)

    def get_glob_parameter(self, key):
        self.glob_parameter['timestamp'] = str(int(time.time() * 1000))
        self.glob_parameter["timetime"] = str(int(time.time()))
        self.glob_parameter['random_phone'] = "1" + \
                                              str(random.randint(3, 9)) + \
                                              str(random.randint(0, 9)) + \
                                              time.strftime('%d%H%M%S')
        return self.glob_parameter.get(key)

    def repalce_parameter(self, text):
        """替换参数--> 可以替换多个~,满足{{$参数}}规则的会被替换"""
        parameter_key = re.findall(r'{{\$(\w+)}}', text)
        for param in parameter_key:
            value = self.get_glob_parameter(param)
            to = rf"{value}"
            text = re.sub(rf'{{{{\${param}}}}}', lambda m: to, text)
        return text


if __name__ == "__main__":
    bl = BuildInLibrary()
    bl.set_glob_parameter("{{username}}", "admin")
    bl.set_glob_parameter("{{password}}", "123456")
    username = bl.get_glob_parameter("username")
    password = bl.get_glob_parameter("password")
    text = "{{$username}} + {{$password}} + {{$timetime}}"
    t = bl.repalce_parameter(text)
    print(t)
