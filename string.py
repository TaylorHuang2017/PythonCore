name = 'jason'
city = 'beijing'
text = "welcome to jike shijian"

s1 = 'hello'
s2 = "hello"
s3 = """hello"""
s1 == s2 == s3
True

"I'm a student"

# 三引号字符串通常用于函数的注释

def calculate_similarity(item1, item2):
    """
    Calculate similarity between two items
    Args:
        item1: 1st item
        item2: 2nd item
    Returns:
      similarity score between item1 and item2
    """

# 转义字符

s = 'a\nb\tc'
print(s)
a
b	c
len(s)
5

name = 'jason'
name[0]
'j'
name[1:3]
'as'

for char in name:
    print(char)   
j
a
s
o
n

# 与C#一样 字符串是不可变的

s = 'hello'
s[0] = 'H'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

# 把第一个字符'h' 改为大写的 'H'
s = 'H' + s[1:] # 第一种方法
s = s.replace('h', 'H') # 第二种方法

# Python中没有与stringbuilder对应的数据类型

# 字符串拼接

str1 += str2  # 表示 str1 = str1 + str2

s = ''
for n in range(0, 100000):
    s += str(n)

# 字符串拼接 join函数

l = []
for n in range(0, 100000):
    l.append(str(n))
l = ' '.join(l) 

# split()

def query_data(namespace, table):
    """
    given namespace and table, query database to get corresponding
    data         
    """

path = 'hive://ads/training_table'
namespace = path.split('//')[1].split('/')[0] # 返回'ads'
table = path.split('//')[1].split('/')[1] # 返回 'training_table'
data = query_data(namespace, table) 

# 去掉首尾字符串

s = ' my name is jason '
s.strip()
'my name is jason'

# 字符串的格式化，有点类似C#中的 string.format()

print('no data available for person with id: {}, name: {}'.format(id, name))
print('no data available for person with id: %d, name: %s' % (id, name))


# 三种拼接方法，最后一个效率最高

s = ''
for n in range(0, 100000):
    s += str(n)

l = []
for n in range(0, 100000):
    l.append(str(n))
    
s = ' '.join(l)

s = " ".join(map(str, range(0, 10000)))   # 把列表 0 ~ 9999 映射到str()函数，即把他们转换为字符串，再逐个用空格拼接


-----------------代码区-----------------
import time

start_time = time.time()
s = ''
for n in range(0, 1000000):
    s += str(n)

end_time = time.time()
print(end_time-start_time)


start_time1 = time.time()
l = []
for n in range(0, 1000000):
    l.append(str(n))

s = ' '.join(l)
end_time1 = time.time()
print(end_time1-start_time1)

-----------------结果区-----------------
0.4459269046783447
0.39172983169555664