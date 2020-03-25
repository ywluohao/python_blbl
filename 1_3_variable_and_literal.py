# Python Variables and Literals

# Variables

number = 100
print(number)

number = 1.23
print(number)

# Python : type inferred language

a,b,c = 100, 1.23, "sdf"
print(a)
print(b)
print(c)

print(a,b,c)

aa = bb = cc = 4
print(aa,bb,cc)

# 1. cc = 4
# 2. bb = cc,
# 3. aa = bb

# Constants

# c++ int const a = 123
# Python : NO

PI = 3.14
GRAVITY = 9.8

# Literals
# constant, can not change
# numeric literal: integer, float, complex
# string literal: string
# boolean literal: True, False
# special: None

# numeric literal

# integer
a = 0b1010      # binary literal
b = 100         # decimal literal
c = 0o310       # octal literal
d = 0x12c       # hexadecimal literal

print(a,b,c,d)


# float
float_1 = 1.25
float_2 = 1.5e2   # 1.5*(10^2)

print(float_1,float_2)

# complex
x = 1 + 2j
print(x)
print(x.imag)
print(x.real)


# string
string_1 = 'Smith'
string_2 = "Smith V2"
string_3 = """ this is really
               a string"""

print(string_1)
print(string_2)
print(string_3)


unicode = u'\u00dcnic\u00f6de'
print(unicode)
print(u'\u00dc')
print('\u00dc')

raw_string = r'raw \t string'
print(raw_string)

not_raw_string = 'raw \t string'
print(not_raw_string)

print(r'\u00dc')

print('new \n line')

# boolean

print(1 == 1)
print(1 == 2)

print(1 == True)
print(0 == False)

# False: 0, 0.0, , ...
print('' == False)

x = ( 1 == True )
y = ( 1 == False )

print(x)
print(y)

a = True + 4
b = False + 10

print(a)
print(b)

print(2 == True)
print(2 == False)

print(False == 0.0)

# special: None

# literal collections
# list, tuple, dict, set

fruits = ['apple', 'banana', 'orange']                      # list
number = (1, 2, 3, 4, 5)                                    # tuple
alphabet = {'a': "apple", 'b': "banana", 'c': "orange"}     # dict key-value pair
set = {'a', 'b', 'c'}                                       # set

print(fruits)
print(number)
print(alphabet)
print(set)
