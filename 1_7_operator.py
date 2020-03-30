# Python Operator

# Arithmetic Operator: +, -, *, /, %, //, **
# Comparison Operator: <, >, ==, !=, <=, >=
# logical operator: and, or, not
# bitwise operator: &, |, ^, ~, <<, >>,
# assignment Operator: =, +=, -=, *=, /=, //=, %=, &=, |=, ^=, <<=, >>=
# identify Operator: is, is not
# membership Operator: in, not in

# Arithmetic Operator: +, -, *, /, %, //, **

print(2+3, 2-3, sep='\t')
print(2*3, 2/3, sep='\t')
print(3/2)
print(3.0/2)

print(3*2)
print(3.0*2)

print(3+2.0)

# 100 / 7 = 14 ... 2
print(100//7, 100%7, sep='\t')
print(7*14+2)

print(2**10)
print(2**20)

# import math;
# math.log

# Comparison Operator: <, >, ==, !=, <=, >=

x, y = 1, 2
print(x>y)
print(x<y)
print(x==y)
print(x!=y)
print(x<=y)
print(x>=y)

x, y = 3, 3
print(x>y)
print(x<y)
print(x==y)
print(x!=y)
print(x<=y)
print(x>=y)

# logical operators: and, or, not

print(True and True)
print(True and False)
print(False and True)
print(False and False)

## True and True -> True; otherwise, False

print(True or True)
print(True or False)
print(False or True)
print(False or False)

## False and False -> False; otherwise, True

print(not True)
print(not False)

print(1>2)
print(2>3)

print((1>2) and (2>3))
print((1>2) and (2<3))
print((1>2) or (2<3))
print(not (2>3))

print((1>2) and (2>3) and (3<4))

# a = 2 + 3 * 4
# a = (2 + 3) * 4

# ()  >  and   >  or

print(True and True or False)

print(True and False or False)

print(True or False and False)

print((True or False) and False)
print(True or (False and False))

# ()  >  not > and   >  or

print(True and not False)
print(not True or True)
print((not True) or True)
print(not (True or True))

# bitwise operators

# & bitwise and
# | bitwise or
# ~ bitwise not
# ^ bitwise xor
# >> bitwise right shift
# << bitwise left shift

# 1 | 1 -> 1
# 1 ^ 1 -> 0

# 1 | 0 -> 1
# 1 ^ 0 -> 1

x = 10; y = 4
bin(x)
bin(y)

# x dec: 10; bin: 1010
# y dec: 4;  bin: 0100

# x & y:
# 1010
# 0100
# -----
# 0000

print(x & y)

# x | y:
# 1010
# 0100
# -----
# 1110

print(0b1110)

print(x | y)

bin(3)


# 10 | 3:
# 1010
# 0011
# -----
# 1011

print(0b1011)
print(10 | 3)

# ~ 10 (bitwise not)
#   1010
# -(1010 + 1)
# - 1011

print(0b1011)
print(~10)

print(10 + ~10)

# 10 | 3:  (bitwise xor)
# 1010
# 0011
# -----
# 1001

print(0b1001)
print(10 ^ 3)

# >> right
# 1011
# 101
# 10

print(11>>2)

# 1011
# 10110
# 101100

print(11<<2)
print(0b101100)


# assignment Operator:

a = 5
print(a)
a = 5 + 1
print(a)

a = a + 1
print(a)

a = a - 5
print(a)




b = 100
b += 1  # b = b + 1
print(b)
b -= 30
print(b)

b *= 2
print(b)

b //= 5
print(b)

b %= 3
print(b)

b += 3
print(b)

b **= 3 # b = b ** 3
print(b)

# =, +=, -=, *=, /=, //=, %=, &=, |=, ^=, <<=, >>=


print(1==1.0)
print(1 is 1.0)
print(1 is int(1.0))

x, y = 1,1
print(x is y)

x, y = 'hello','hello'
print(x is y)
print(x is not y)

x, y = [1,2], [1,2]
print(x is y)
print(x == y)

print(id(x))
print(id(y))

xs, ys = 'hi', 'hi'
print(id(xs))
print(id(ys))


x = [1,2]
y = x

print(id(x))
print(id(y))
print(x is y)


# in, not in

print('h' in 'hello')

print('H' in 'hello')

print(1 in [1,2,3])

print(4 in [1,2,3])
print(4 not in [1,2,3])
