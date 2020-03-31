# Python for loop

# sequence: list, tuple, string, .......

# syntax:
# for val in sequence:
#     do statments

fruit_list = ['apple', 'banana', 'pear', 'orange']

for fruit in fruit_list:
    print(fruit)
print('end of the for loop')

# 1. fruit = 'apple'
# 2. fruit = 'banana'
# ...

sum_of_fruit_letter = 0

for fruit in fruit_list:
    print(f'{fruit} has length {len(fruit)}')
    sum_of_fruit_letter += len(fruit)
print(f'the total sum of fruit letter is {sum_of_fruit_letter}')

a_long_string = 'an apple a day keeps doctor away!'
count_a = 0
count_o = 0
for char in a_long_string:
    if char == 'a':
        count_a += 1
    elif char == 'o':
        count_o += 1
print(f'"{a_long_string}" has {count_a} a and {count_o} o')

# 'an apple a day keeps doctor away!'
#  1  2     3  4               5 6

# reslut:
# {'a': 6, 'o':2,  ... }

# range()
# range(stop) -> range object
# range(start, stop[, step]) -> range object

help(range)

# range(stop) -> range object
# range(start, stop[, step]) -> range object

print(range(3))
print(range(3,6))
print(range(3,6,2))

print(list(range(3)))
print(list(range(3,6)))
print(list(range(3,6,2)))

print(list(range(10)))
print(list(range(0,10,2)))

sum_of_number = 0
sum_of_squared = 0
for i in range(5):
    print(f'{i} squared is {i**2}')
    sum_of_number += i
    print(f'the sum of numbers from 0 to {i} is {sum_of_number}')
    sum_of_squared += i**2
    print(f'the sum of number squared from 0 to {i} is {sum_of_squared}')

sum_of_number = 0
sum_of_squared = 0
for i in range(1,101):
    sum_of_number += i
    sum_of_squared += i**2
print(f'the sum of numbers from 1 to {i} is {sum_of_number}')
print(f'the sum of number squared from 1 to {i} is {sum_of_squared}')

print(i)

sum_of_number = 0
sum_of_squared = 0
for i in range(1,101,2):
    sum_of_number += i
    sum_of_squared += i**2
print(f'the sum of numbers from 1 to {i} is {sum_of_number}')
print(f'the sum of number squared from 1 to {i} is {sum_of_squared}')

sum_of_number = 0
sum_of_squared = 0
for i in range(2,101,2):
    sum_of_number += i
    sum_of_squared += i**2
print(f'the sum of numbers from 2 to {i} is {sum_of_number}')
print(f'the sum of number squared from 2 to {i} is {sum_of_squared}')

# for ... else

sum_of_number = 0
sum_of_squared = 0
for i in range(2,101,2):
    sum_of_number += i
    sum_of_squared += i**2
else:
    print(f'the sum of numbers from 2 to {i} is {sum_of_number}')
    print(f'the sum of number squared from 2 to {i} is {sum_of_squared}')


# enumerate
help(enumerate)

fruit_list = ['apple', 'banana', 'pear', 'orange']
print(enumerate(fruit_list))
print(list(enumerate(fruit_list)))

for (i, fruit) in enumerate(fruit_list):
    print(f'{fruit} has id {i}')


print(list(enumerate(fruit_list, 1)))
print(list(enumerate(fruit_list, start=1)))

for (i, fruit) in enumerate(fruit_list, 2):
    print(f'{fruit} has id {i}')

for i in range(len(fruit_list)):
    print(f'{fruit_list[i]} has id {i}')

for i in range(2, 2+len(fruit_list)):
    print(f'{fruit_list[i-2]} has id {i}')
