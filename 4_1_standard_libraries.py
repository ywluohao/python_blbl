

# https://docs.python.org/3/tutorial/stdlib.html


# os: operating system


import os
os.getcwd() # current working directory

# win
# 'C:\\Python39'
# 'C:/Python39'

os.mkdir('new_folder')  # make directory

os.listdir(".")

os.chdir('new_folder')

os.getcwd()

# directory
# absolute directory path: '/Users/hao/Desktop/python/new_folder'
# relative directory path:

os.listdir("..")

os.chdir('..')
os.getcwd()

dir(os)

import shutil
help(shutil.move)

os.getcwd()

import glob
glob.glob('aa.*')


os.listdir()

glob.glob('ex*.py')
glob.glob('*.py')

input()

print("hello")

# regular expression


'tea for too'.replace('too', 'two')


import re
re.findall(r'\b[fF][a-z]*', 'For foot or hand fell fastest')

re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

re.findall(r'(\b[a-z]+) \1','cat in the the hat')

import statistics


dir(statistics)

# numpy, scipy, pandas,

# web scraping
#







import datetime
dir(datetime)


from datetime import date, datetime
now = date.today()
print(now)
now

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

now.strftime("%m_%d_%y")

a = datetime.strptime("20210316", "%Y%m%d")
print(a)


birthday = date(1964, 7, 31)
print(birthday)
age = now - birthday
age.days
dir(age)
type(age)

import timeit
"-".join(str(n) for n in range(100))


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests


print(average([20, 30, 70]))

print(1)
print('1')
print("hello")
repr("hello")
repr(1)
repr('1')

print("hello"*10)
repr("hello "*100)

import reprlib
reprlib.repr("hello "*100)

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]

print(t)

pprint.pprint(t)

pprint.pprint(t, width=30)

from pprint import  pprint as pp

pp(t, width=30)

import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

doc
print(doc)


print(textwrap.fill(doc, width=40))


a = [1,2,3]
b = a

b[1] ="heelo"
a

del a
b

2**8

# [-128, 127]
# [0, 255]

2**16

from array import array
a = array('H', [4000, 10, 700, 65535])
sum(a)
a[1:3]

1.1+2.2 == 3.3
1.1+2.2

from decimal import  Decimal as D
D("1.1")+D("2.2") == D("3.3")

round(0.735,2)
0.7*1.05
-1.225 * 100

_ + 0.5
#
