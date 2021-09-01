man = {
  "first_name" : "wei",
  "last_name" : "tong",
  "age" : 40,
  "city" : "Hangzhou",
}
print(man)
for key, value in man.items():
    print(key)
    print(value)

for key in man.keys():
    print(key)

for key in man:
    print(key)


print(man.keys())
print(man.values())