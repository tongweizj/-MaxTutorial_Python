"""
this is wtong's frist code
python 能用中文注释吗？
"""
import sys
import pickle

def print_lol(the_list, indent=False, level=0, fn=sys.stdout ):
	"""
	print_lol can print every item in a list
	"""
	for each_item in the_list : 
		if isinstance(each_item, list):			
			print_lol(each_item, indent, level+1, fn)
			
		else :
			if indent:
				for tab_stop in range(level):
					print("\t", end='', file=fn)

			with open(fn, 'wb') as dumpdata :
				pickle.dump(each_item,dumpdata)
			# print(each_item,file = fn )