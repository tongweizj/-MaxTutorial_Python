# 列表 List

## 1. list 基本属性

``` python
movies = ["hello", 1975, "world",91,["2 level",["3 level", "2","3"]]]
```

## 2. list元素的增删改查

### 2.1 列表元素的访问

``` python
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam",91,["Graham Chapman",["Michael Palin", "John Cleese","Terry Gilliam","Eric Idle"]]]

# 索引访问
data = movies[0]   #取出数据
data = movies[0][1]  #取出下层列表中的数据

# 访问最后一个元素
print(movies[-1])
data = movies.pop() # 取出最后一位数据
```
### 切片访问
``` python
c = movies[1:3] # 取出从movies[1]开始，一共3个数组成员
```
### 2.2 list元素的 删改查

####  添加

``` python
tb = ['1','2','3','4']

## 添加
tb.append('5') # 添加在末尾,不返回

## 插入

movies.insert(5,11)    # 添加指定次序,原部分list往后移一位

movies.extend([9,8])   # 添加一个列表合并队尾
```
####  删除

``` python
movies.remove('9')   # 删除 指定元素
del tb[5] # 删除 指定位置
```

#### pop
``` python
tb = ['1','2','3','4']
print(tb)
print(tb.pop())  # 取出+删除 最后一位数据
print(tb.pop(1)) # 取出1位置
print(tb)
```

### 2.3 组织列表

**列表按照大小，永久排序**
``` python
tb = [9, 1, -4, 3, 7, 11, 3]

tb.sort() # 从小到大排序
print('tb：', tb)

tb.sort(reverse=True)  # 从大到小排序
print('tb：', tb)
```

**列表按照大小，临时排序**
``` python
tb = [9, 1, -4, 3, 7, 11, 3]

tb2 = sorted(tb) # 从小到大排序
print('tb2：', tb2)

tb3 = sorted(tb,reverse=True)  # 从大到小排序
print('tb3：', tb3)
```

**列表永久翻转**
list3 = [1, 2, 3]
list3.reverse()
print('list3=', list3)



## for 遍历列表

``` python
list1 = [9, 1, -4, 3, 7, 11, 3]
for x in list1:
  print(x)
```

## range()

``` python
for x in range(1,5):  # 不包含5
  print(x)

list2 =list(range(1,10))
print(list2)
```

## 列表解析
``` python
squares = [value**2 for value in range(1,11)]
print(squares)

squares = []
for value in range(1,11):
  squares.append(value**2)
print(squares)
```

## 复制列表

``` python
tb = list(range(1,11))
print(tb)
tb2 = tb[:]
print(tb2)
tb2.append(21)
print(tb) # 没有变化
print(tb2)
```


## 3. 常用方法

### 两个列表相加
``` python
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam",91,["Graham Chapman",["Michael Palin", "John Cleese","Terry Gilliam","Eric Idle"]]]


movies.extend([9,8])   # 添加一个列表合并队尾
```
### 获取列表的一些基本信息
``` python
list1 = [9, 1, -4, 3, 7, 11, 3]

print('list1的长度 =', len(list1))

print('list1里的最大值=', max(list1))

print('list1里的最小值 =', min(list1))

print('list1里3这个元素一共出现了{}次'.format(list1.count(3)))



```