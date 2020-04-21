# break, continue, pass
#

# break
# syntax:

# for var in sequence:
#     # code for loop
#     if condition:
#         # code for if condition
#         break
#     # code for loop

for char in "string":
    print(char, "line 1")
    if char == "i":
        print(char, 'line 2')
        break
        print(char, 'line 3')
    print(char, 'line 4')
print(char, 'line 5')

num = 5
while num > 0:
    print(num, 'line 1')
    num -= 1

num = 5
while num > 0:
    print(num, 'line 1')
    num -= 1
    if num == 3:
        break
print(num, 'line 2')


# continue
for char in "string":
    print(char, "line 1")
    if char == "i":
        print(char, 'line 2')
        continue
        print(char, 'line 3')
    print(char, 'line 4')
print(char, 'line 5')

sum_num = 0
sum_sqd = 0
for i in range(20):
    if i % 3 == 0:
        continue
    print(i)
    sum_num += i
    sum_sqd += i ** 2
print(sum_num, sum_sqd)


sum_num = 0
sum_sqd = 0
for i in range(20):
    if i % 3 != 0:
        print(i)
        sum_num += i
        sum_sqd += i ** 2
print(sum_num, sum_sqd)


num = 5
while num > 0:
    print(num, 'line 1')
    num -= 1
    if num == 3:
        continue
print(num, 'line 2')

num = 5
while num > 0:
    print(num, 'line 1')
    num -= 1
    if num == 3:
        continue
    print(num, 'line 11')
print(num, 'line 2')

num = 5
while num > 0:
    print(num, 'line 1')
    num -= 1
    if num == 3:
        break
    print(num, 'line 11')
print(num, 'line 2')



# pass

print('line 1')
for i in 'string':
    pass
print('line 2')

def func(arguments):
    pass

class Example:
    pass

num = 5
while num > 0:
    pass


print('line 1')
for i in 'string':
    print('i')
    pass
print('line 2')



print('line 1')
for i in 'string':

print('line 2')
