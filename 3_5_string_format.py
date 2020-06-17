String format

# % <- c language
# "  ".format()
# f-string: f''


# "   ".format(p0, p1, ..., k0=v0, k1=v1, ...)
# positional argument : p0, p1, ...
# keyword argument: k0=v0, k1=v1, ...  -> f-string f' {k0:k1}  '

# default argument :
print('Hello {}, your balance is {:9.3f}'.format('Adam', 230.2346))

# positional argument :

print('Hello {0}, your balance is {1:9.3f}'.format('Adam', 230.2346))
print('Hello {0:9s}, your balance is {1:9.3f}'.format('Adam', 230.2346))


print('Hello {1}, your balance is {0:9.3f}'.format(230.2346, 'Adam'))

# keyword argument:

print('Hello {name}, your balance is {balance:9.3f}'.format(name='Adam', balance=230.2346))

# f-string:
name='Adam'
balance=230.2346
print(f'Hello {name}, your balance is {balance:9.3f}')

print(f'Hello {"Adam"}, your balance is {230.2346:9.3f}')

# mixed argument:
print('Hello {}, your balance is {balance:9.3f}'.format('Adam', balance=230.2346))

# number format

# https://docs.python.org/3/library/string.html#grammar-token-grouping-option
# number format specifer

# integer
print('{:b}'.format(123))
bin(123)
print('{:#b}'.format(123))

print('{:c}'.format(123))
chr(123)
ord('{')

print('{:d}'.format(123))
print('{:o}'.format(123))
oct(123)
print('{:x}'.format(123))
print('{:X}'.format(123))
hex(123)
print('{:#X}'.format(123))
print('{:d}'.format(123))

print('{:d}'.format(0o173))


# float and decimal
print('{:e}'.format(123))
print('{:e}'.format(123.456))
print('{:E}'.format(123.456))
print('{:f}'.format(123.456))

print('{:}'.format(123.456))

float('nan')
float('NaN')

print('{:%}'.format(0.023))

# padding, precision

print('{:5d}'.format(123))
print('{:5s}'.format("123"))

print('{:8.3f}'.format(1.2345))

print('{:08.3f}'.format(1.2345))

print('{:1d}'.format(123))
print('{:6d}'.format(123))
print('{:06d}'.format(123))

# sign: + , - , space

print('{:+f} {:+f}'.format(12.34, -12.34))
print('{:-f} {:-f}'.format(12.34, -12.34))
print('{: f} {: f}'.format(12.34, -12.34))

# alignment: <, ^, >, =
print('{:5d}'.format(12))
print('{:<5d}'.format(12))
print('{:^5d}'.format(12))
print('{:=+5d}'.format(12))
print('{:=8.2f}'.format(-12.3))

print('{:5}'.format('hi'))
print('{:>5}'.format('hi'))
print('{:^5}'.format('hi'))

# fill: symbol no {}
print('{:_^5}'.format('hi'))
print('{:=^8}'.format('hi'))

print('{:<5d}'.format(12))
print('{:0<5d}'.format(12))
print('{:!<5d}'.format(12))
print('{::<5d}'.format(12))


# string
print('{:.3}'.format('hello world'))
print('{:5.3}'.format('hello world'))
print('{:>5.3}'.format('hello world'))
print('{:_>5.3}'.format('hello world'))


# thousand seperator ,  12345678 -> 12,345,678
print('{:,}'.format(12345678))
print('{:_}'.format(12345678))
print('{:_x}'.format(12345678))
print('{:x}'.format(12345))
print('{:_b}'.format(12345))
print('{:b}'.format(12345))




# format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
# fill            ::=  <any character>
# align           ::=  "<" | ">" | "=" | "^"
# sign            ::=  "+" | "-" | " "
# width           ::=  digit+
# grouping_option ::=  "_" | ","
# precision       ::=  digit+
# type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"


print('{:10,.2f}'.format(1234.5678))
print('{:010,.2f}'.format(1234.5678))
print('{:+010,.2f}'.format(1234.5678))
print('{:=+10,.2f}'.format(1234.5678))
print('{:_=+15,.2f}'.format(1234.5678))
print('{:_= 15,.2f}'.format(1234.5678))
print('{:_= 15_.2f}'.format(1234.5678))

# {   :}
# empty  -> default positional
# digit  -> positional
# keyword

print('{0:_= 15_.2f}'.format(1234.5678))
print('{num:_= 15_.2f}'.format(num=1234.5678))

# str(), repr()
str(123)
repr(123)

str('hi')
repr('hi')
repr(repr('hi'))

print('{:s}'.format('hi'))

print('{!r:s}'.format('hi'))
print('{!s:s}'.format('hi'))

print('{0!r:s}'.format('hi'))
print('{name!r:s}'.format(name='hi'))



# override
a = 1
a =2
a

def hi():
    print('hello')

hi()

def hi():
    print(repr('hello'))
hi()

# datetime
import datetime

date = datetime.datetime.now()
date

print("now is {:%Y/%m/%d %H:%M:%S}".format(date))
print("now is {:%H:%M:%S, %B %d, %Y}".format(date))
