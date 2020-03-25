# 1.2 Statement, Identation, and Comments

# Statement
# assignment statement
a = 1

# if statement, while statement ................

# multi-line statement:
# explicit: \ (line continuation character)
aa = 1 + 2 + 3 + \
     4 + 5 + 6 + \
     7 + 8 + 9
print(aa)

# implicit: (), [], {}

aaa = (1 + 2 + 3 +
       4 + 5 + 6 +
       7 + 8 + 9 )
print(aaa)

colors_1 = ['red', 'green', 'yellow', 'blue']
colors_2 = ['red',
            'green',
            'yellow',
            'blue']

print(colors_1)
print(colors_2)


# multiple statements in one line ;
a1 = 1; a2 = 2; a3 = 3; a4 = 4

a1 = 1
a2 = 2
a3 = 3
a4 = 4


# identations

for i in range(1, 11):
    print(i)
    if i == 5:
        print('this is 5')
    print(i)


for i in range(1, 11):
    print(i)
    if i == 5:
        print('this is 5')
        print(i)


# Comment

as1 = 12 # as2 = 2
print(as1)
print(as2)

# multi-line comment

# az1 = 12
# az2 = 22
# az3 = 23

'''
az1 = 12
az2 = 22
az3 = 23
'''

# docstring : documentation string

def double(num):
    '''funciton to double the number'''
    return 2*num


print(double(4))
print(double.__doc__)
