# 创建 {}

d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male') 
d1 == d2 == d3 ==d4
True

s1 = {1, 2, 3}
s2 = Set([1, 2, 3])
s1 == s2
True

s = {1, 'hello', 5.0}

# 元素访问

d = {'name': 'jason', 'age': 20}
d['name']
'jason'
d['location']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'location'

d = {'name': 'jason', 'age': 20}
d.get('name')
'jason'
d.get('location', 'null')   # 指定如果键不存在时，返回的默认值是什么
'null'

# 字典，集合，本质上是哈希表，其查找性能远优于列表

# 字典 集合 都是无序的，因此不支持索引操作
s = {1, 2, 3}
s[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing

# 用 in 判断是否存在

s = {1, 2, 3}
1 in s
True
10 in s
False

d = {'name': 'jason', 'age': 20}
'name' in d
True
'location' in d
False

# 增删改

d = {'name': 'jason', 'age': 20}
d['gender'] = 'male' # 增加元素对'gender': 'male'
d['dob'] = '1999-02-01' # 增加元素对'dob': '1999-02-01'
d
{'name': 'jason', 'age': 20, 'gender': 'male', 'dob': '1999-02-01'}
d['dob'] = '1998-01-01' # 更新键'dob'对应的值 
d.pop('dob') # 删除键为'dob'的元素对
'1998-01-01'
d
{'name': 'jason', 'age': 20, 'gender': 'male'}

s = {1, 2, 3}
s.add(4) # 增加元素 4 到集合
s
{1, 2, 3, 4}
s.remove(4) # 从集合中删除元素 4
s
{1, 2, 3}


# 排序

d = {'b': 1, 'a': 2, 'c': 10}
d_sorted_by_key = sorted(d.items(), key=lambda x: x[0]) # 根据字典键的升序排序
d_sorted_by_value = sorted(d.items(), key=lambda x: x[1]) # 根据字典值的升序排序
d_sorted_by_key
[('a', 2), ('b', 1), ('c', 10)]
d_sorted_by_value
[('b', 1), ('a', 2), ('c', 10)]

s = {3, 4, 2, 1}
sorted(s) # 对集合的元素进行升序排序
[1, 2, 3, 4]




# 给定商品的 Id， 找出其价格
def find_product_price(products, product_id):
    for id, price in products:
        if id == product_id:
            return price
    return None 
     
products = [
    (143121312, 100), 
    (432314553, 30),
    (32421912367, 150) 
]

print('The price of product 432314553 is {}'.format(find_product_price(products, 432314553)))

# 输出
The price of product 432314553 is 30


products = {
  143121312: 100,
  432314553: 30,
  32421912367: 150
}
print('The price of product 432314553 is {}'.format(products[432314553])) 

# 输出
The price of product 432314553 is 30

# 找出这些商品有多少不同的价格

# list version
def find_unique_price_using_list(products):
    unique_price_list = []
    for _, price in products: # A
        if price not in unique_price_list: #B
            unique_price_list.append(price)
    return len(unique_price_list)

products = [
    (143121312, 100), 
    (432314553, 30),
    (32421912367, 150),
    (937153201, 30)
]
print('number of unique price is: {}'.format(find_unique_price_using_list(products)))

# 输出
number of unique price is: 3

# set version
def find_unique_price_using_set(products):
    unique_price_set = set()
    for _, price in products:
        unique_price_set.add(price)
    return len(unique_price_set)        

products = [
    (143121312, 100), 
    (432314553, 30),
    (32421912367, 150),
    (937153201, 30)
]
print('number of unique price is: {}'.format(find_unique_price_using_set(products)))

# 输出
number of unique price is: 3

# 性能比较

import time
id = [x for x in range(0, 100000)]
price = [x for x in range(200000, 300000)]
products = list(zip(id, price))

# 计算列表版本的时间
start_using_list = time.perf_counter()
find_unique_price_using_list(products)
end_using_list = time.perf_counter()
print("time elapse using list: {}".format(end_using_list - start_using_list))
## 输出
time elapse using list: 41.61519479751587

# 计算集合版本的时间
start_using_set = time.perf_counter()
find_unique_price_using_set(products)
end_using_set = time.perf_counter()
print("time elapse using set: {}".format(end_using_set - start_using_set))
# 输出
time elapse using set: 0.008238077163696289

# 字典的key不可以是列表，因为他是不可变的
