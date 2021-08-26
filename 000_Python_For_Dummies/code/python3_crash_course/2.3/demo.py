name = 'Max'
message = f'Hello {name},would you like to learn some Python today?'
print(message) 

print(name.lower())
print(name.upper())
print(name.title())

### 2-5

name = 'Max'
topic = 'Hello, did you had lunch today?'
message = f'{name} once said, "{topic}"'
print(message)

### 2-7
name = '\t   max  \n'
print(name.lstrip())
print(name.rstrip())
print(name.strip())