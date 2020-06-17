# Python set

# unordered
# unique
# set is mutable, not hashable
# set element is hashable -> immutable

# operation

# frozenset: immutable

# create a set
s1 = {1,2,3}
type(s1)
s12 = {1,'asd',(1,2)}
s13 = {1,'asd', [1]}

s2 = set([1,2,3])
s2

s22= set('asd')
s22

# set(), tuple(), list(), ''.join(iterable),

s3 = {}
type(s3)

s31 = set()
type(s31)

len(s3)

# modify a set
s4 = set('abcde')
s4


s4.add('xyz')
s4

s4.update('opq')
s4

# remove

del s1
s1

s4
s4.remove('a')
s4

s4.remove('x')

s4.discard('b')
s4
s4.discard('x')
s4

help(s4.pop)


s4
s4.pop()
s4
s4.pop()
s4
s4.pop()
s4


set().pop()

# A: {1,2,3}
# B: {2,3,4}
# C: {2,3}
# D: {4}

# subset:   <= C is a subset of A
# superset: >= A is a superset of C
# disjoint:    C is a disjoint with D

# union:                A | B: {1,2,3,4}
# intersection:         A & B: {2,3}
# difference:           A - B: {1}
# symmetric difference: A ^ B: = (A | B) - (A & B) = {1,4}

a = {1,2,3,4}
b = {2,4,6,8}
c = {3,5,7,9}
d = {2,4}
e = {2,4}

a.isdisjoint(b)
a.isdisjoint(c)
b.isdisjoint(c)

d.issubset(a)
d <= a
d.issubset(e)
d <= e
d < e

d < a

a.issuperset(d)
d > e
d >= e

a
b
c
d

a.union(b)
a.union(b).union(c)
a | b | c

a.intersection(b)
a&b
a&b&c

a.difference(b)
a-b
a-b-c
a.difference(b).difference(c)

a.symmetric_difference(b)
a^b^c

a | b & c

(a | b) & c

# bitwise and or xor
# - > & > ^ > |

# = , copy()

x = set('abc')
x

x1 = x
id(x)
id(x1)

x1 = x1 | a
x1
x

id(x1)

x2 = x
x2 |= a
x2
x
id(x2)


x = set('abc')
x3 = x.copy()
x
x3
id(x)
id(x3)

x1 = x
x1.clear()
x

# update:
# | -> |=  update
# & -> &=  intersection_update
# - -> -=  difference_update
# ^ -> ^=  symmetric_difference_update


dir(a)


a = {1,2,3,4}
b = {2,4,6,8}
c = {3,5,7,9}
d = {2,4}

a &= b
a

a -= c
a
a -= b
a

a.update(b)
a

x = {1,2,3,4}
y = x
y ^= c
x
y

z = {1,2,3,4}
x = z

z = z^c
z
x
