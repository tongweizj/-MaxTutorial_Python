# for x in range(1,21):
#   print(x)

# number_list = list(range(1,1_000_000))
# for x in number_list:
#   print(x)

# print(min(number_list))
# print(max(number_list))
# print(sum(number_list))

# tb = list(range(1,20,2))
# for x in tb:
#   print(x)

# tb = list(range(3,31,3))
# for x in tb:
#   print(x)

# tb = list(range(1,11))
# tb2=[]
# for x in tb:
#   tb2.append(x**3)
# print(tb2)

# tb3 = [x**3 for x in range(1,11)]
# print(tb3)

tb = list(range(1,11))
print(tb)
tb2 = tb[:]
print(tb2)
tb2.append(21)
print(tb)
print(tb2)
