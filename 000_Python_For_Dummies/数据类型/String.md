# 字符串

## 定义

```
# 两种引号都可以，可以相互嵌套
''
""
```

## 常用方法

```python
message = 'Hello wold!'
message.title() // 单词首字母变大写
message.upper() // 所有字母变大写
message.lower() // 所有字母变小写
// 去空白
message.strip() // 去掉开头和结尾的空格，中间的不去
message.rstrip() // 去掉右侧的空格
message.lstrip() // 去掉左侧的空格
```



## 字符串中添加变量

### 新方法 f""

```python
message = 'Hello wold!'
last_name = 'tong'
first_name = 'wei'
message = f"{last_name} {first_name}" // {} 里是可执行的语句
```

### 老方法 format()
```python
last_name = 'tong'
first_name = 'wei'
full_name = "{} {}".format(last_name,first_name) // 用format里的变量替换“”里的{}
```

### 制表符
```python
message= 'tong'
message = '\twei' // \转译 t制表符
```

### 换行符
```python
message= 'tong'
message = '\nwei' // \转译 n换行
```

## 常见问题

### 字符串查找
```python
a = '1234569064323'
if '64' in a:
   print('Yes')
 else:
   print('No')
 
#Yes
```

### 字符串替换

```python
lines = []
with open(filename) as file_python:
  lines = file_python.readlines()
for line in lines:
  print(line.strip().replace('Python','C'))  # 前一个参数是被替换的字符串
```