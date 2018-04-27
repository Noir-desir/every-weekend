#! usr/bin/python
# _*_ coding=utf-8 _*_
'''
@time: 2018/4/27 10:51
@author: jiangzeyu5
'''

import os, re, random

path = os.getcwd()

files_list = []
for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        files_list.append(os.path.join(root, name))
print(files_list)

def writedown():
    for file in files_list:
        if 'py' not in file:
            with open(file, 'w+') as f:
                result = '13' + str(random.randint(100000000, 999999999))
                f.write(result)
                f.closed

def replace():
    pattern = re.compile(r'(\d{2})\w+(\d{4})', re.S)
    for file in files_list:
        if 'py' not in file:
            with open(file, 'r') as f1:
                content = f1.read()
                f1.closed
            with open(file, 'w') as f2:
                result = re.sub(pattern, r'\1******\2', content,1)
                f2.write(result)
                f2.closed

if __name__ == '__main__':
    # writedown()
    replace()
