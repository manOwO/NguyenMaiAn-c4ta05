# 1
'''
so1 = int(input("1st number: "))
so2 = int(input("2nd number: "))
sum = so1 + so2
print("Sum:", sum)
'''

# 2
'''
year = int(input("year: "))
if year%4 == 0:
    print(year, "is a leap year")
    # print('year {} is a leap year'.format(year))
else:
    print(year, "is not a leap year")
    # print('year {} is not a leap year'.format(year))
'''
# 3
'''
num = int(input("any intergers: "))
for i in range (2,num):
    if num%i == 0:
        print(num, "is not a prime number")
        # print('year {} is not a prime number'.format(num))
        break
    else:
        print(num, "is a prime number")
        # print('year {} is a prime number'.format(num))
        break
'''

    # cách a chữa
'''
num = int(input("any intergers: "))
counter = 0
for i in range (2,num):
    if num%i == 0:
        counter += 1 aka counter = counter + 1
if counter == 0:
    print('{} is primative'.format(num))
else:
    print('{} is not primative'.format(num))

'''
# some operator
'''
modulus (chia lấy phần bù (só dư)) = number % 4 
floor_division (chia lấy phần nguyên) = number // 4
'''
'''
print('{} is {} years old'.format(name, age))
'''
# neww
'''
number = input("enter a number: ")
muahaha = True
while muahaha:
    number = input("enter a number: ")
    try:
        number1 = int(number)
        muahaha = False
    except ValueError:
        print('you have entered an invalid input.')
'''

# 4
''' 
loop = 0
while loop < 20:
    loop = loop + 1
    print(loop)
'''

# 5
'''
loop = 0
while loop < 20:
    loop = loop + 2
    print(loop)
'''
'''
loop = 0
while loop < 20:
    loop = loop + 1
    true = loop%2
    while true == 0:
        print(loop)
        break
'''
'''
for i in range (2,20,2):
    print(i)
'''
# 6
'''
loop = 0
while loop > -20:
    loop = loop - 2
    print(loop)
'''
'''
loop = 20
while loop > 0:
    loop = loop - 1
    true = loop%2
    while true == 0:
        print(loop)
        break
'''
'''
for i in range (20,2,-2):
    print(i)
'''

# 7
'''
muahaha = True
while muahaha:
    num = input("enter a number: ")
    try:
        number1 = int(num)
        muahaha = False
    except ValueError:
        print('you have entered an invalid input.')
if muahaha == False:
    num2 = 0
    while number1 > 0:
        number1 = number1 // 10
        num2 += 1
print(num2)
'''

# 8
'''
low = 1
high = 100
while True:
    ppl = (ppl1+ppl2)//2
    print("is {} the number you're thinking?".format(ppl))
    inp = input("Correct (c), larger (l) or smaller (s): ")
    if inp == "c":
        break
    if inp == "l":
        low = ppl
    if inp == "s":
        high = ppl
'''