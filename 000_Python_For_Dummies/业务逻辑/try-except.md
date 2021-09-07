# 异常处理

## 基本

```python
"""ZeroDivisionError"""
print(5/0)

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
```

```python
try:
  print(5/0)
except ZeroDivisionError:
  print(You cannot divide by zero!")
```

try 不阻止后续代码的运行
避免崩溃


## try-except-else

尝试（try）
万一（excepy）
正常就（else）

```python
try:
  print(5/0)
except ZeroDivisionError:
  print(You cannot divide by zero!")
else:
  print(You have a answer!) #这里是try代码正常运行后，下一步运行的代码
```

## FileNotFoundError

```python
filename = 'alice.txt'

try:
  with open(filename, encoding = 'utf-8') as f:
    contents = f.read()
except fileNotFoundError:
  print(f"Sorry, the file{filename} does not exist.")  

```

## 静默失败 pass

```python

def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        --snip--
    except fileNotFoundError:
        pass
    else:
        --snip--  

```
遇到错误的情况下
因为是pass，所以不做任何处理
这样就实现了静默失败