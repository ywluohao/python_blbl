# List

# string

# list: []
# tuple: ()
# set: {}  / frozenset()
# dict: {key:value; ...}

# immutable, mutable
# in :
# len(): length


# construct a list
# method 1: square bracket:
a1 = [1,2,3]
# method 2: list(iterable)
a2 = list('abcde')
print(a2)
a3 = list((1,2,3))
print(a3)
a4 = list({1,2,3})
print(a4)
print(list({3,2,1}))


range(1,10,2)
list(range(1,10,2))

# method 3:from some function


a5 = [1,2,2.0, 'asr', [1,2,3], (1,2)]
len(a5)

# index operator: []

for i in range(len(a5)):
    print(a5[i])

for item in a5:
    print(item)


a5
a5[0]
a5[0:2]


a6 = list(range(0,10,1))
a6
# [i=0:j=len(l):k=1]
a6[3]
a6[:3]
a6[:3:2]
a6[::2]

a6[-1]
a6[-2]
a6[:-3]

a6[::-1]

a6[::-2]

a6[1.0]

a6[int(10/3)]

dir(a6)


a = [1,2,3]
a.append(4)
a

a.extend([11,22])
a

a.append([100,200])
a

a += [-1,-2]
a

b = list('abc')
b

b *= 3
b

c = list('hello')
c

c * 2
c

d = [1,2,3]
help(d.insert)


d.insert(1,'hello')
d

d.insert(10,'world')
d

# a += b # a = a + b

[1] + [2,3]
[2,3] + [100, 101]

# concatenate

a

a[0] = 'hello'
a

a[1:3] = ['AAPL', 'MSFT']
a

del a
a

a = [1,2,3,'abc']
a


b = [12,34]
b.clear()
b
len(b)



dir(a)

a
a.remove(1)
a
a.remove(3)
a
a.remove(4)

if 4 in a:
    a.remove(4)

a = [1,2,3,4,5,6]

b = [2,5,7]

a-b

for item in b:
    if item in a:
        a.remove(item)

a


help(a.pop)

a

a.pop()
a


print(a.remove(3))
a
print(a.pop(0))
a

dir(a)

a = [1,2,3,4]

b = a.copy()
b

c = a
c

d = a[:]
d


# soft copy

a
c


a.append('a')
a
c

id(a)
id(c)

id(b)
id(d)

b
d


a
a[2]
a.index(3)
a.index(5)


a = [1,4,2,7]
a.sort()
a
help(a.sort)

a.sort(reverse=True)
a



a
sorted(a)
a

# sorted(): return a new list
# .sort(): in-place

help(sorted)


dir(a)

a
a.reverse()
a

a = [1,1,2,3,3,4]
a.count(1)
help(a.count)

dir(a)

a

del a[0]
a

del a[-2:]
a

# remove(), pop(), clear()

# list comprehension

a = list(range(0,9))
a

ans =[]
for item in range(0,9):
    ans.append(item ** 2)
ans

[item ** 2 for item in range(0,9)]

[item ** 2 for item in range(0,9) if item % 2 == 0]

# (i,j) 1<=i,j<=4
[(i,j) for i in range(1,5) for j in range(1,5)]

# (i,j) 1<=i<=j<=4

[(i,j) for i in range(1,5) for j in range(1,5) if i <= j]


ans = []
for i in range(1,5):
    for j in range(1,5):
        if i <= j:
            ans.append((i,j))
ans


ans2 = []
for i in range(1,5):
    for j in range(i,5):
        ans2.append((i,j))
ans2
