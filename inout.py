# 键盘输入和输出

name = input('your name:') # 参数是提示语
gender = input('you are a boy?(y/n)')

###### 输入 ######
your name:Jack
you are a boy?

welcome_str = 'Welcome to the matrix {prefix} {name}.'
welcome_dic = {
    'prefix': 'Mr.' if gender == 'y' else 'Mrs',
    'name': name
}

print('authorizing...')
print(welcome_str.format(**welcome_dic))  ## 字典解包成prefix和name, 一种实现可变参数的手段  https://docs.python.org/2.7/tutorial/controlflow.html#unpacking-argument-lists 

########## 输出 ##########
authorizing...
Welcome to the matrix Mr. Jack.


a = input()
1
b = input()
2

print('a + b = {}'.format(a + b))
########## 输出 ##############
a + b = 12
print('type of a is {}, type of b is {}'.format(type(a), type(b)))
########## 输出 ##############
type of a is <class 'str'>, type of b is <class 'str'>
print('a + b = {}'.format(int(a) + int(b)))
########## 输出 ##############
a + b = 3

# 文件输入和输出
# 自然语言处理，1. 读取文件 2. 去除所有标点符号和换行符， 大写变小写 3. 合并相同的词，统计词频，并由大到小排序 4. 输入结果到文件

import re

# 你不用太关心这个函数
def parse(text):
    # 使用正则表达式去除标点符号和换行符
    text = re.sub(r'[^\w ]', '', text)

    # 转为小写
    text = text.lower()
    
    # 生成所有单词的列表
    word_list = text.split(' ')
    
    # 去除空白单词
    word_list = filter(None, word_list) # 过滤空串，0， None，空列表等值
    
    # 生成单词和词频的字典
    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1
    
    # 按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)
    
    return sorted_word_cnt # list of tuples

with open('in.txt', 'r') as fin: # with()语句，任务执行完毕后，会自动调用close()
    text = fin.read()     # 文件所有内容读取到内存中，缺点是不适用于过大的文件，可能造成内存溢出，
    # 更好的方法是指定参数size, 或者用readline()函数

word_and_freq = parse(text)

with open('out.txt', 'w') as fout:
    for word, freq in word_and_freq:
        fout.write('{} {}\n'.format(word, freq))

########## 输出 (省略较长的中间结果) ##########

and 15
be 13
will 11
to 11
the 10
of 10
a 8
we 8
day 6

...

old 1
negro 1
spiritual 1
thank 1
god 1
almighty 1
are 1

# JSON序列化与实战


import json

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}

params_str = json.dumps(params) # 把字典转化成一个字符串 / json序列化

print('after json serialization')
print('type of params_str = {}, params_str = {}'.format(type(params_str), params))

original_params = json.loads(params_str) # 把字符串转化成字典 / json反序列化

print('after json deserialization')
print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))

########## 输出 ##########

after json serialization
type of params_str = <class 'str'>, params_str = {'symbol': '123456', 'type': 'limit', 'price': 123.4, 'amount': 23}
after json deserialization
type of original_params = <class 'dict'>, original_params = {'symbol': '123456', 'type': 'limit', 'price': 123.4, 'amount': 23}




# 输出字符串到文件， 或从文件中读取json字符串

import json

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}

with open('params.json', 'w') as fout:
    params_str = json.dump(params, fout)

with open('params.json', 'r') as fin:
    original_params = json.load(fin)

print('after json deserialization')
print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))

########## 输出 ##########

after json deserialization
type of original_params = <class 'dict'>, original_params = {'symbol': '123456', 'type': 'limit', 'price': 123.4, 'amount': 23}


# 思考题： 计算word count

from collections import defaultdict
import re

f = open("ini.txt", mode="r", encoding="utf-8")
d = defaultdict(int)

for line in f:
    for word in filter(lambda x: x, re.split(r"\s", line)):
        d[word] += 1