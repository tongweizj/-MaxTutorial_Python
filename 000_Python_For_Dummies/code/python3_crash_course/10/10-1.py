filename = './python.txt'
with open(filename) as file_python:
  contents = file_python.read()
  print(contents)

print('\n')
with open(filename) as file_python:
  contents = file_python.readlines()
  for line in contents:
    print(line.strip())

print('\n')
lines = []
with open(filename) as file_python:
  lines = file_python.readlines()
for line in lines:
  print(line.strip())
  
print('\n')
lines = []
with open(filename) as file_python:
  lines = file_python.readlines()
for line in lines:
  print(line.strip().replace('Python','C'))