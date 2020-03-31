# Python while loop

# while loop:
# syntax:

# while test_expression:
#     do somthing

num = 0
while num == 0:
    print(num)
    num -= 1
    print(num)


num = 2
while num > 0:
    print(num)
    num -= 1
    print(num)

# True = 1, no-0 -> True

num = 2
while num:
    print(num)
    num -= 1
    print(num)


num = -2
while num:
    print(num)
    num += 1
    print(num)

sum_num = 0
sum_sqd = 0
num = 0

while num<100:
    num += 1
    sum_num += num
    sum_sqd += num ** 2
print(f'the sum of numbers from 1 to {num} is {sum_num}')
print(f'the sum of numbers squared from 1 to {num} is {sum_sqd}')


sum_num = 0
sum_sqd = 0
num = 0

while num<100:
    num += 2
    sum_num += num
    sum_sqd += num ** 2
print(f'the sum of numbers from 2 to {num} is {sum_num}')
print(f'the sum of numbers squared from 2 to {num} is {sum_sqd}')

# while ... else....


sum_num = 0
sum_sqd = 0
num = 0

while num<100:
    num += 2
    sum_num += num
    sum_sqd += num ** 2
else:
    print(f'the sum of numbers from 2 to {num} is {sum_num}')
    print(f'the sum of numbers squared from 2 to {num} is {sum_sqd}')
