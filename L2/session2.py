# list review
'''
NOTE: index
menu = ['cơm', 'canh', 'thịt']
print(menu[0]) --> 'cơm' 
print(menu[-1]) --> 'thịt'
NOTE: loop item
for item in menu:
    print(item)
NOTE: loop index
for index in enumerate(menu):
    print(index, item)
NOTE: update
menu[0] = "phở"
menu[1], menu[2] = menu[2], menu[1]
NOTE: delete
del menu[1]
''' 

# 1
'''
NOTE: a
'''
from random import randint
input_list = []
for i in range(10):
    input_list.append(randint(1,10))
print(input_list)
'''
NOTE: b
input_listb1=[]
input_listb2=[]
for itemb1 in range(0,3):   
    input_listb1.append(input_list[itemb1])
print(input_listb1)
for itemb2 in range (7,10):
    input_listb2.append(input_list[itemb2])
print(input_listb2)

NOTE: neww
# list slicing
list_a = [1, 4, 2, 7, 3]
    list[số bắt đầu : số stop]
n = 3
list_a = [:n] --> [1, 4, 2]
list_a = [-n:] --> [2, 7, 3]
'''
'''
NOTE: c
'''
    