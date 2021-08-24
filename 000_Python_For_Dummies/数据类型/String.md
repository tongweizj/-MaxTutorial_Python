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


```



## 字符串中添加变量



### 新方法 f""

```
message = 'Hello wold!'
last_name = 'tong'
first_name = 'wei'
message = f"{last_name} {first_name}"
```



### 老方法 format()
