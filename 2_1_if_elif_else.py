# Python Decision Making

# if statement

# if statement:
# syntax:
# if (test expression):
#     statements

num = 3
if num > 0 :
    print(f'{num} is a positive number.')
    print('this is in the if statement.')
print('this is out of the if statement.')

num = -3
if num > 0 :
    print(f'{num} is a positive number.')
    print('this is in the if statement.')
print('this is out of the if statement.')

# if ... else statement
# syntax:
# if (test expression):
#     (if True, expression)
# else:
#     (if False, expression)

num = 3
if num > 0 :
    print(f'{num} is a positive number.')
    print('this is in the if statement while True.')
else:
    print(f'{num} is a negative number or zero.')
    print('this is in the if statement while False.')
print('this is out of the if statement.')

num = -3
if num > 0 :
    print(f'{num} is a positive number.')
    print('this is in the if statement while True.')
else:
    print(f'{num} is a negative number or zero.')
    print('this is in the if statement while False.')
print('this is out of the if statement.')

# nested if

num = 3
if num > 0 :
    print(f'{num} is a positive number.')
    print('this is in the if statement while True.')
else:
    print('go into the second if statement.')
    if num == 0:
        print(f'{num} is zero.')
        print('this is in the second if statement while True.')
    else:
        print(f'{num} is a negative number.')
        print('this is in the second if statement while False.')
    print('this is out of the second if statement.')
print('this is out of the first if statement.')

num = 0
if num > 0 :
    print(f'{num} is a positive number.')
    print('this is in the if statement while True.')
else:
    print('go into the second if statement.')
    if num == 0:
        print(f'{num} is zero.')
        print('this is in the second if statement while True.')
    else:
        print(f'{num} is a negative number.')
        print('this is in the second if statement while False.')
    print('this is out of the second if statement.')
print('this is out of the first if statement.')

num = -2
if num > 0 :
    print(f'{num} is a positive number.')
    print('this is in the if statement while True.')
else:
    print('go into the second if statement.')
    if num == 0:
        print(f'{num} is zero.')
        print('this is in the second if statement while True.')
    else:
        print(f'{num} is a negative number.')
        print('this is in the second if statement while False.')
    print('this is out of the second if statement.')
print('this is out of the first if statement.')

# nested if -> else if -> elif

num = 2
if num > 0 :
    print(f'{num} is a positive number.')
    print('this is in the if statement while True.')
elif num == 0:
    print(f'{num} is zero.')
    print('this is in the elif statement while True.')
else:
    print(f'{num} is a negative number.')
    print('this is in the elif statement while False.')
print('this is out of the if statement.')

num = 0
if num > 0 :
    print(f'{num} is a positive number.')
    print('this is in the if statement while True.')
elif num == 0:
    print(f'{num} is zero.')
    print('this is in the elif statement while True.')
else:
    print(f'{num} is a negative number.')
    print('this is in the elif statement while False.')
print('this is out of the if statement.')

num = -2
if num > 0 :
    print(f'{num} is a positive number.')
    print('this is in the if statement while True.')
elif num == 0:
    print(f'{num} is zero.')
    print('this is in the elif statement while True.')
else:
    print(f'{num} is a negative number.')
    print('this is in the elif statement while False.')
print('this is out of the if statement.')

# if
# if else
# if elif else
# if elif

num = -2
if num > 0 :
    print(f'{num} is a positive number.')
    print('this is in the if statement while True.')
elif num == 0:
    print(f'{num} is zero.')
    print('this is in the elif statement while True.')
print('this is out of the if statement.')

if 1:
    print("This is True")

if 0:
    print("This is True")

num = 0
if num:
    print('This is True')
else:
    print('This is False')

num = -1
if num:
    print('This is True')
else:
    print('This is False')


string = ''
if string:
    print('This is True')
else:
    print('This is False')


string = 'a'
if string:
    print('This is True')
else:
    print('This is False')

list = []
if list:
    print('This is True')
else:
    print('This is False')


list = []
if len(list) != 0:
    print('This is True')
else:
    print('This is False')


list = [1,2]
if list:
    print('This is True')
else:
    print('This is False')


list = [1,2]
if len(list) != 0:
    print('This is True')
else:
    print('This is False')
