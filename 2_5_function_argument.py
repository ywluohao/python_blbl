# Python Function and Argument

# z = add(x,y)
#

# syntax:
# def function_name(parameters):
#     """docstring"""
#     statements
#    [return None]

def greet(name):
    """
    this function is used to greet.
    ths input is a string
    """
    print(f'Hello {name}, Good morning!')
    print(f'How are you? {name}')

greet('Paul')
greet('John')

name = "Paul"
print(f'Hello {name}, Good morning!')
print(f'How are you? {name}')


name = "John"
print(f'Hello {name}, Good morning!')
print(f'How are you? {name}')

# docstring
dir(greet)


print(greet.__doc__)

print(greet.__name__)



def sum_h(x , y):
    """ enter two numbers, get the sum"""
    return x + y

print(sum_h(1, 2))
print(greet('Paul'))

x
def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num

print(absolute_value(-1))
print(absolute_value(1000))
abs(-100)


def absolute_value(num):
    if num >= 0:
        print(f'the absolute value of {num} is {num}')
        return num
        print('line 1')
    else:
        print(f'the absolute value of {num} is {-num}')
        return -num
        print('line 2')
    print('line 3')

absolute_value(-1)
print('line 4')

a = 100
a

a = 100
print(a)

a = 100
a
b = 100


def absolute_value(num):
    if num >= 0:
        print(f'the absolute value of {num} is {num}')
        return num
        print('line 1')
    else:
        print(f'the absolute value of {num} is {-num}')
        return -num
        print('line 2')
    print('line 3')

absolute_value(-1)
print('line 4')

print(absolute_value(-1))
print('line 4')

aa = absolute_value(-1)
print(aa)
aa

absolute_value(1)
print('line 4')

print(absolute_value(1))
print('line 4')


# function
# built-in: int(), abs(), print(), input(), len(),
type(print)
type(abs)


# user-defined function
type(greet)
type(absolute_value)

def add_h(x, y):
    return x + y

print(add_h(1,2))


def add_h_default(x, y=0):
    return x + y

print(add_h_default(1,2))
print(add_h_default(1))


def add_h_default(x=0, y):
    return x + y

def add_h_default(x, y=0, z=2, k =3):
    return x + y + z + k

print(add_h_default(1))
print(add_h_default(1,100))
print(add_h_default(1,100, 10000))
print(add_h_default(1,100, 10000, -1))

def add_h_default(x = 8, y=0, z, k =3):
    return x + y + z + k

help(print)

def add_h_default(x, y=0, z=2, k =3):
    return x + y + 2*z + k

# keyword argument

print(add_h_default(x = 1, y = 100, z = 10000))
print(add_h_default(z = 1, y = 100, x = 10000))


# positional argument
print(add_h_default(1,100, 10000))

# positional argument + keyword argument
print(add_h_default(1,100, k =1000))
print(add_h_default(1,100, k =1000, z= -100))
