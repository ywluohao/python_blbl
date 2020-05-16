# tuple

# list : mutable (add, delete, change)
# tuple : immutable

# list function/method:
# list()
# len(), in, [i:j:k]
# .append(), .extend(), +=, *=, .insert()
# del , del[i:j:k], .remove(), .pop(), .clear()
# .index(), .sort(), sorted(), .reversed(), .copy(), .count()

# tuple: immutable
# tuple(), len(), in, [i:j:k]
# del, .index(), .count()

dir(tuple)

# tuple : ()  -> ,

a1 = (1,2)
a2 = (1)
print(f'a1 has type {type(a1)} and a2 has type {type(a2)}')

(1) == 1

b1 = 1,2
b2 = 1,
print(f'b1 has type {type(b1)} and b2 has type {type(b2)}')

len(a2)
len(b2)

a3 = (1,)
type(a3)

# tuple packing, tuple unpacking

c1 = 1,2,3,'apple'
a,b,c,d = c1
print(a)
print(d)

[x , y] = [1, 2]
x
y

xx, yy = 11, 22
xx
yy

a11 = 10
a12 = 20

a12, a11 = a11, a12
a11
a12

# tuple() - constructor


tuple([1,2,3])
tuple('hello')

a = tuple('hello123')
a

a[0]
a[-1]

a[0] = 'w'

a.index('l')
a.count('l')

a = a[:a.index('l')] + ('k',) + a[a.index('l')+1:]
a


b = tuple('hello123')
bb = list(b)
bb[bb.index('l')] = 'k'
tuple(bb)

# +=  x
# +, *

('a',) *3
('a') *3




b
del b
b


c

'h' in c
len(c)

for i, n in enumerate(c, start=1):
    print(i, n)

list(enumerate(c, start=1))

[x ** 2 for x in range(5)]

(x ** 2 for x in range(5))

a = b
a = b[:]
