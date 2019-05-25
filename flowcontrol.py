# 求 y = x的绝对值

# y = |x|
if x < 0:
    y = -x
else:
    y = x


# 和 C#不同， Python不支持switch语句
# 多个条件判断用 elif

if condition_1:
    statement_1
elif condition_2:
    statement_2
...
elif condition_i:
    statement_i
else:
    statement_n

# 除了boolean类型的数据，条件判断最好是显性的

if i != 0:
    ...

# 而不是

if i:
    ...

# 循环语句，相当于 C# 中的 foreach

l = [1, 2, 3, 4]
for item in l:
    print(item)
1
2
3
4

# 遍历可迭代对象

for item in <iterable>:
    ...

# 字典的遍历

d = {'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}
for k in d: # 遍历字典的键
    print(k)
name
dob
gender

for v in d.values(): # 遍历字典的值
    print(v)
jason
2000-01-01
male    

for k, v in d.items(): # 遍历字典的键值对
    print('key: {}, value: {}'.format(k, v))
key: name, value: jason
key: dob, value: 2000-01-01
key: gender, value: male 


# 通过索引遍历

l = [1, 2, 3, 4, 5, 6, 7]
for index in range(0, len(l)):
    if index < 5:
        print(l[index])        
        
1
2
3
4
5


# 遍历时同时返回索引和元素  enumerate() 

l = [1, 2, 3, 4, 5, 6, 7]
for index, item in enumerate(l):
    if index < 5:
        print(item)  
              
1
2
3
4
5

# Continue / break
# Continue  跳出本次循环，继续下面的循环  break完全退出循环

#  找出 价格小于1000 且颜色不是红色的所有产品名称和颜色的组合

# 方案一： 不用continue

# name_price: 产品名称 (str) 到价格 (int) 的映射字典
# name_color: 产品名字 (str) 到颜色 (list of str) 的映射字典
for name, price in name_price.items():
    if price < 1000:
        if name in name_color:
            for color in name_color[name]:
                if color != 'red':
                    print('name: {}, color: {}'.format(name, color))
        else:
            print('name: {}, color: {}'.format(name, 'None'))


# 方案二： 用continue

# name_price: 产品名称 (str) 到价格 (int) 的映射字典
# name_color: 产品名字 (str) 到颜色 (list of str) 的映射字典
for name, price in name_price.items():
    if price >= 1000:
        continue
    if name not in name_color:
        print('name: {}, color: {}'.format(name, 'None'))
        continue
    for color in name_color[name]:
        if color == 'red':
            continue
        print('name: {}, color: {}'.format(name, color))


# 循环  for / while

l = [1, 2, 3, 4]
index = 0
while index < len(l):
    print(l[index])
    index += 1

# while : 在满足某个条件前，不停地重复某些操作，不针对特定的集合
# for: 遍历集合，找出满足条件的元素

while True:
    try:
        text = input('Please enter your questions, enter "q" to exit')
        if text == 'q':
            print('Exit system')
            break
        ...
        ...
        print(response)
    except as err:
        print('Encountered error: {}'.format(err))
        break 


# 条件和循环并做一行

expression1 if condition else expression2 for item in iterable

# 等同于

for item in iterable:
    if condition:
        expression1
    else:
        expression2

# 列表生成式

y = [value * 2 + 5 if value > 0 else -value * 2 + 5 for value in x]

# 将文件中逐行读取的一个完整语句，按逗号分隔单词，去掉首位的空字符，并过滤掉长度小等于3的单词，最后返回由单词组成的列表

text = ' Today,  is, Sunday'
text_list = [s.strip() for s in text.split(',') if len(s.strip()) > 3]
print(text_list)
['Today', 'Sunday']


# 给定两个列表 x, y ， 返回x, y中所有元素组成的元组

[(xx, yy) for xx in x for yy in y if xx != yy]

# 思考题，针对values中每一组子列表，输出其和attributes中的键对应后的字典，最后返回字典组成的列表

attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'], 
['mike', '1999-01-01', 'male'],
['nancy', '2001-02-01', 'female']
]

# expected outout:
[{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}, 
{'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'}, 
{'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]


[dict(zip(attributes,v)) for v in values]   # 函数式编程

循环版：
l = []
for value in values:
    d = {}
    for i in range(3):
        d[attributes[i]] = value[i]
    l.append(d)