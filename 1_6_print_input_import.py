# Python I/O and import

# input: input()
# output: print()


print('this is a sentence.')

a = 5

print("a is", a)

help(print)

# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

print(1,2,3,4)
print('a', 'b', 'c')
print('a', 'b', 'c', sep='   ')

# \t: tab; \n: new line

print('a', 'b', 'c',      sep='\t')
print('aaa', 'b', 'c',    sep='\t')

print('a', 'b', end='\t')
print('a', 'b', end='\t')

print('a', 'b', end='\n')
print('a', 'b', end='\n')

print('a', 'b')
print('a', 'b')

print('a')
print('b')
print('c')


print('a', end='\t')
print('b', end='\t')
print('c', end='\t')

print('a', end='\t')
print('b')
print('c', end='\t')
print('d')

name = 'Tony'
age = 18
pi = 3.14159265358979323846

print(name, 'is', age, 'years old and', name, 'konws pi is', pi)


# 3 methods to better print string : string format

# c-style : %
# format():
# f foramt: python 3.5

# c-style : %: %s: str; %d: interger; %f: float

print('%s is %d years old' %(name, age))

# format()

print('{} is {} years old'.format(name, age))

# f format

print(f'{name} is {age} years old')


# float format: eg: .2f
name = 'Tony'
age = 18
pi = 3.14159265358979323846


print('%s is %d years old and %s knows pi is %f' %(name, age, name, pi))
print('%s is %d years old and %s knows pi is %.2f' %(name, age, name, pi))

print('{} is {} years old and {} knows pi is {:.2f}'.format(name, age, name, pi))
print('{:s} is {} years old and {} knows pi is {:.2f}'.format(name, age, name, pi))

print(f'{name} is {age} years old and {name} knows pi is {pi:.2f}')


### input: input([prompt])

userName = input("Enter User Name:")
print(userName)
print(type(userName))

print(f'userName has value {userName} and type {type(userName)}')

aa = input()

print(f'aa has value {aa} and type {type(aa)}')

# int()

aa = int(input("Enter a number: "))
print(f'aa has value {aa} and type {type(aa)}')


expr = input("Enter an expression: ")
print(f'expr has value {expr} and type {type(expr)}')

#eval(): evaluate
print(eval('1+2'))

help(eval)


print(f'eval(expr) has value {eval(expr)} and type {type(eval(expr))}')

# python import
# .py is a library

import math

dir(math)

print(math.pi)
print(math.sqrt(4))
print(math.e)

help(math.sqrt)

help(math.pi)

help(math)
