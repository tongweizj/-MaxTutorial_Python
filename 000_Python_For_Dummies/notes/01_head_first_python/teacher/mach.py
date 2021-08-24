
import btime

with open('james.txt','r') as james :
	list = james.readline().split(',')
	james_list = []
	for each_item in list :
		record = btime.sanitize(each_item)
		james_list.append(record)
	
	print(sorted(james_list))



