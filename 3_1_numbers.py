# Python Numbers

# int: 5
# float: 1.2
# complex: 1+2j

# type()
# isinstance()

# help()
# .__doc__
# dir()

a = 1 + 5j
type(a)
isinstance(a, int)
isinstance(a, complex)

type(a) == complex

b = complex()
b

a.real
a.imag

a.__doc__

c = a.conjugate()
c
a

dir(a)


help(a)

# int 100
# float: accurate to 15th

(1.1 + 2.2) == 3.3
(1.2 + 2.1) == 3.3

1.1 + 2.2

# 0.5
# 0.25
# 0.125
# 0.0625

# 0.1 = 0.5*0+0.25*0+0.125*0+0.0625*1+...

# 0.1 -> 0.00011001100110011...

import decimal
print(0.1)
print(decimal.Decimal(0.1))
print(decimal.Decimal('0.1'))

from decimal import Decimal as D
D(1.1)
D(2.2)
D(1.1) + D(2.2)

D(2.1) + D(1.2)

D('1.1') + D('2.2')
D('2.1') + D('1.2')

D('2.1') + D('1.20')

# 1.2  -<< 1.15 - 1.24
# 1.20 -<< 1.195 - 1.204

D('2.1') * D('1.20')

print(D('2.1') * D('1.20'))


2.1 * 1.20


# 1/3 =~ 0.3333...

from fractions import Fraction as F

F(1.5)
print(F(1.5))

type(F(1.5))


'a\tb'
print('a\tb')

F(1.5)
F(3,2)
F(1,3)
print(F(1,3))

F(1.1)
D(1.1)


D('1.1')
F('1.1')
print(F('1.1'))

print(F('1.1')+F('1.1'))
print(1/F('1.1'))
print(1/F('1.1')>0)

import math

math.pi
math.e
math.cos(math.pi)
math.exp(10)
math.log10(10000)
math.log(3)
math.factorial(10)

# 10! = 10*9*8*...*1
dir(math)

import random
dir(random)

help(random.randint)

random.randint(1,100)

help(random.random)

random.random()

help(random.randrange)

list(range(1,100,2))[0:5]

random.randrange(1,100,2)

for _ in range(5):
    print(random.randrange(1,100,2))


dir(random)

x = list('abcde')
x

random.shuffle(x)
x

for _ in range(5):
    random.shuffle(x)
    print(x)

help(random.choice)

for _ in range(5):
    print(random.choice(x))

help(random.choices)

for _ in range(10):
    print(random.choices(x, k=3))


for _ in range(10):
    random.shuffle(x)
    print(x[0:3])

x =list('abcde')
for _ in range(10):
    print(random.choices(x, [0.1,0.1,0.1,0.1,0.6]))

x =list('abcde')

for _ in range(10):
    print(random.choices(x, cum_weights=[0.1,0.2,0.3,0.3,1]))
