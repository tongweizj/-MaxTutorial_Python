# while

- 只有满足条件时，循环才停止
- 必须写好条件，否则会变成死循环

```python
>>> while current_number <= 5:
...     print(current_number)
...     current_number += 1
... 
1
2
3
4
5
```

## 终止循环的方法

1. 标志
```python
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
```
在active 改为False后，会继续运行后续的代码

2. break

```python

while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)
```

break 后，直接跳出循环

3. continue

```python
current_number= 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)
... 
1
3
5
7
9
```
continue 不跳出循环，但下面的代码不运行了，
所以上面代码的含义就是偶数就不打印了

## list 的遍历
for 循环总是用某个规则将list完整的遍历一次
但while不是，他不一定，更灵活。可以满足条件就跳出，也可以永远不退出。