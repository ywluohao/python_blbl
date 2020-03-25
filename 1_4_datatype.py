# Python Data Type

# class: int
# instance(object):

a = 1
# a is an instance of a class "int",

# type(obj) -> type of class

print(type(a))


# Python Number:
# int, float, complex

a,b,c = 5, 2.1, 1+3j
print(a, "is of type", type(a))
print(b, "is of type", type(b))
print(c, "is of type", type(c))

# isinstance(obj, type)  -> bool
print(isinstance(1, int))
print(isinstance(c, complex))
print(isinstance(b, int))

# float is accurate up to 15 decimal places
aa = 0.1234567890123456789
print(aa)

# Python List
a1 = 1
a2 = 2
a3 = 3

a_list = [1,2,3]

# ordered: start from 0
print(a_list[0])
print(a_list[2])

# []: slicing operator
# [i=0:j=-1:k=1]: start from i, length = j-i,

a_list = [1,2,3,4,5,6,7]
print(a_list[0])                    # a_list[0:-1:1]
print(a_list[0:2])
print(a_list[:2])

print(a_list)
print(a_list[::2])
print(a_list[:4:2])

print(a_list[1:3])

mixed_list =[1,2,3, 4.0, 'str', True, None]
for item in mixed_list:
    print(item, "is of type", type(item))

# mutable : can be changed

print(a_list)
a_list[0] =1000
print(a_list)

a_list[:2] = ['a1', 'a2']
print(a_list)

# tuple: ordered but not mutable
t = (1, 2, 'string', True)
print(type(t))
print(type(t[0]))
print(type(t[-1]))

t[0] = 1000


# string: ordered

s ="Hello world!"
print(s, type(s))
print(s[0])
print(s[-1])
print(s[3:6])
print(s[::2])

s[0] = 'G'

s = "Gello"
print(s)

# set: unordered, unique

a = {2,3,0,6}
print(a)

a[0]

aa = {1,1,1,1,1,2,3,3,3}
print(aa)

bb = {1,2,3,'abs'}
print(bb)


# dictionary: unordered, key-value pair, mutable

d = {"ON": "Ontario", "AB": "Albert"}
print(d["ON"])
print(d)

d2 = {"AB": "Albert", "ON": "Ontario"}
print(d2)

print(d == d2)


d = {"ON": "Ontario", "ON": "Ontario1","AB": "Albert"}
print(d)

print(d)

d["AB"] = "another province"
print(d)



# number, string,
# list, tuple, set, dict
