# Python string

a = 'hello world'

# index
len(a)
a[2]
a[-1]
a[3:8]
a[:8]
a[8:]
a[::2]
a[::-1]

# loop
for i,c in enumerate(a):
    print(f'{i}:\t{c}')

# immutable
a
a[0] = 'd'

id(a)

a = 'd' + a[1:]
a
id(a)

list_a = list(a)
list_a

id(list_a)
list_a[0] = 'z'
list_a
id(list_a)

del a
a


a = 'hi everyone'
a = a[3:]
a

dir(a)


a.capitalize()
a
help(a.capitalize)

a = a.capitalize()
a


a.upper()
a.lower()
a

a.isupper()
a.islower()
a.istitle()

a.title()

i = '1'
i.isdigit()
i.isalpha()

help(i.isalpha)

i.isnumeric()
help(i.isnumeric)

i = '\57'
print(i)

i.isascii()
i.isalnum()

# function

count
find
index
partition
replace
rfind, rindex, rsplit, rpartition

split, strip

aa = 'hello world, hi everyone.'
list(enumerate(aa))


aa.count('h')
aa.find('w')
aa.index('w')
aa.find('c')
aa.index('c')
help(aa.find)
aa.find('w',7)
aa.index('w',7)

aa.partition('w')
aa.partition('wo')
aa.partition('wa')


aa.split('w')
aa.split('o')
help(aa.split)
aa.split('o', 2)
aa.split('o', 5)

aa
aa.strip('h')
aa.strip('he.')

b = '   \n    abc     \t  '
print(b)

b.strip()
help(b.strip)

aa

aa.find('o')
aa.rfind('o')
aa.split('o')
aa.rsplit('o')
aa.split('o', 1)
aa.rsplit('o', 1)
aa.partition('o')
aa.rpartition('o')


aa
aa.replace('hello', 'HELLO')
aa.replace('hello1', 'HELLO')
aa.replace('o', '123')

help(aa.replace)




'o' in aa


# quotation mark
a1 = "a"
a2 = 'a'
a3 = " Bob says 'hello'  "
a3

# docstring """    """

a4 = '1'
a4 + a4
a4 + ' hello'
a4 * 10

# %   c
# .format()
# f''


# escape character
# \n new line
# \t tab
# \\

a5 = 'hello\tworld'
a5
print(a5)
print('hello\\tworld')
print(r'hello\tworld')

# encode, decode
# ascii, utf-8

# \ooo \xhh

print('!')
print('\041')
print('\x21')

join ljust zfill

dir(aa)



# list -> string: join
# string -> list: list

list('hello')
str(['h','e'])

''.join(['h','e'])
','.join(['h','e'])
'\t'.join(['h','e'])
print('\t'.join(['h','e']))

a = ['hello', 'hi', 'welcome']
for item in a:
    print(item)
for item in a:
    print(item.rjust(10))

help(aa.rjust)

for item in a:
    print(item.rjust(10, "_"))

for item in a:
    print(item.rjust(10, "_"), " @ ", item.ljust(10, "_"))






help(aa.zfill)

"123".zfill(8)



# escape characters

# \'


aaa = " bob says \"hello\" \t"
