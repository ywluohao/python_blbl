# Python Type Conversion and Type Casting

# 1. implicit type conversions
# 2. explicit type conversions [type casting]

# implicit type conversions:
# avoid data loss

num_int = 1
num_float = 1.1

num_sum = num_int + num_float

print(num_sum)

print(type(num_int))
print(type(num_float))
print(type(num_sum))


num_str = '123'

num_new_2 = num_int + num_str

# explicit type conversions [type casting]

num_new_3 = num_int + int(num_str)

print(type(num_new_3), num_new_3)

# int(), float(), str()

i = 1
f = 1.23
s1 = '12'
s2 = '1.234'

print(float(i))
print(str(i))

# int -> float, str

print(int(f))
print(int(1.9))
print(str(f))

# float -> int, str

print(int(s1))
print(int(s2))

print(float(s2))
print(float(s1))


# list, tuple, set, dict

l = [1, 2, 3]
print(set(l))
print(tuple(l))

t = (1,2,3)
print(list(t))
print(set(t))

s = {1,2,3}
print(list(s))
print(tuple(s))


l2 = [1,1,2,3]
print(set(l2))
