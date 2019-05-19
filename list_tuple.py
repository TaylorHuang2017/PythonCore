# 列表是动态的，可以修改
# 元组是静态的，不可以修改

l = [1, 2, 'hello', 'world'] # 列表中同时含有 int 和 string 类型的元素
l
[1, 2, 'hello', 'world']

tup = ('jason', 22) # 元组中同时含有 int 和 string 类型的元素
tup
('jason', 22)

l = [1, 2, 3, 4]
l[3] = 40 # 和很多语言类似，python 中索引同样从 0 开始，l[3] 表示访问列表的第四个元素
l
[1, 2, 3, 40]

tup = (1, 2, 3, 4)
tup[3] = 40
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

tup = (1, 2, 3, 4)
new_tup = tup + (5, ) # 创建新的元组 new_tup，并依次填充原元组的值
new _tup
(1, 2, 3, 4, 5)

l = [1, 2, 3, 4]
l.append(5) # 添加元素 5 到原列表的末尾
l
[1, 2, 3, 4, 5]

l = [1, 2, 3, 4]
l[-1]
4

tup = (1, 2, 3, 4)
tup[-1]
4

list = [1, 2, 3, 4]
l[1:3] # 返回列表中索引从 1 到 2 的子列表
[2, 3]

tup = (1, 2, 3, 4)
tup[1:3] # 返回元组中索引从 1 到 2 的子元组
(2, 3) 

l = [[1, 2, 3], [4, 5]] # 列表的每一个元素也是一个列表

tup = ((1, 2, 3), (4, 5, 6)) # 元组的每一个元素也是一元组

list((1, 2, 3))
[1, 2, 3]

tuple([1, 2, 3])
(1, 2, 3)

# 列表和元组的常用内置函数

l = [3, 2, 3, 7, 8, 1]
l.count(3) 
2
l.index(7)
3
l.reverse()
l
[1, 8, 7, 3, 2, 3]
l.sort()
l
[1, 2, 3, 3, 7, 8]

tup = (3, 2, 3, 7, 8, 1)
tup.count(3)
2
tup.index(7)
3
list(reversed(tup))
[1, 8, 7, 3, 2, 3]
sorted(tup)
[1, 2, 3, 3, 7, 8]

# 即使放置相同的元素，元组的存储空间要比列表少，这是元组的一个优点
# 列表是动态的，因此需要存储指向每个元素的指针（占8字节），还需要存储已经分配的长度大小以追踪列表空间的使用情况（占8字节）

l = []
l.__sizeof__() // 空列表的存储空间为 40 字节
40
l.append(1)
l.__sizeof__() 
72 // 加入了元素 1 之后，列表为其分配了可以存储 4 个元素的空间 (72 - 40)/8 = 4
l.append(2) 
l.__sizeof__()
72 // 由于之前分配了空间，所以加入元素 2，列表空间不变
l.append(3)
l.__sizeof__() 
72 // 同上
l.append(4)
l.__sizeof__() 
72 // 同上
l.append(5)
l.__sizeof__() 
104 // 加入元素 5 之后，列表的空间不足，所以又额外分配了可以存储 4 个元素的空间

# 列表和元组的性能

python3 -m timeit 'x=(1,2,3,4,5,6)'
20000000 loops, best of 5: 9.97 nsec per loop
python3 -m timeit 'x=[1,2,3,4,5,6]'
5000000 loops, best of 5: 50.1 nsec per loop

python3 -m timeit -s 'x=[1,2,3,4,5,6]' 'y=x[3]'
10000000 loops, best of 5: 22.2 nsec per loop
python3 -m timeit -s 'x=(1,2,3,4,5,6)' 'y=x[3]'
10000000 loops, best of 5: 21.9 nsec per loop

# 列表和元组的使用场景

def get_location():
    ..... 
    return (longitude, latitude)

viewer_owner_id_list = [] # 里面的每个元素记录了这个 viewer 一周内看过的所有 owner 的 id
records = queryDB(viewer_id) # 索引数据库，拿到某个 viewer 一周内的日志
for record in records:
    viewer_owner_id_list.append(record.id)
