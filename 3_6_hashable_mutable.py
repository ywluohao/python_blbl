# number: int, float, complex
# bool, None

# str:  "abc"
# list: [1,2,3]
# tuple: (1,2,3)
# set:   {1,2,3}
# dict:  {"a":1}

# frozenset

# mutable:  list, set, dict,
# immutable: str, tuple, frozenset

l1 = [1,2,3]
id(l1)
l1 += [4]
id(l1)
l1

s1 = 'abc'
id(s1)
s1 += 'd'
id(s1)


l1[0] = 'asd'
l1

s1[0] = 'd'

# hash function

# hashable -> immutable

# hashable ~~ immutable

# a -> b

hash(1)
hash(1.0)
hash(True)

1 == True
hash(True) == hash(1)


hash('a')
hash(8207602368369663481)

'a' == 8207602368369663481

# hash() depends on Python version

id(1)
id(True)


hash([1])

# tuple: every element is hashable -> tuple is hashable

t1 = (1,2,(1,3))
hash(t1)
t2 = (1,2,[1,3])
hash(t2)



# set:
s1 = {1,2,t1}
s1

s2 = {1,2,t2}

# dict key -> hashable
d1 = {t1:123}
d1

d2 = {t2:123}
