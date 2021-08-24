from nester import print_lol
man = []
other = []
                
try:
        data = open('sketch.txt') 
        for each_line in data:
                try:
                        (role, line_spoken) = each_line.split(':',1)
                        line_spoken = line_spoken.strip()
                        if role == 'Man' :
                                man.append(line_spoken)
                        
                        elif role == 'Other Man':
                                other.append(line_spoken)
                        else :
                                pass
                except ValueError as err:
                        print('value error is:'+str(err))

        data.close()
except IOError :
        print("The data file is missing:")

# try:
#         indent = False
#         fn = 'man_data.txt'
#         print_lol(man, indent, 0, fn)
#         print_lol(other,indent, 0, 'other_data.txt')
#         # with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file :
#         #         indent=False
#         #         print_lol(man, indent, 0, man_file)

#         #         print_lol(other, indent,0,other_file )

#                 # for each_line in man :
#                 #         if isinstance(each_line,list):
#                 #                 pass
#                 #         else : 
#                 #                 print(each_line, file = man_file)

#                 # for each_line in other :
#                 #         if isinstance(each_line,list):
#                 #                 pass
#                 #         else : 
#                 #                 print(each_line, file=other_file)                
                

# except IOError :
#         print('file error:')

import pickle
with open('man_data.txt', 'wb') as man_file , open('other_data.txt', 'wb') as other_file :
        # a_list = pickle.load(man_file)
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)


# print(a_list)