# Python Recursion and lambda function

# factorial: !          4! = 4 * 3 * 2 * 1 = 24 = 4 * 3!
# n! = n * (n-1)!   ... 1! = 1

def cacl_factorial(n):
    if n == 1:
        return 1
    else:
        return n * cacl_factorial(n-1)

print(cacl_factorial(4))
print(cacl_factorial(1))

def cacl_factorial(n):
    if n == 1:
        print(n)
        return 1
    else:
        print(n)
        return n * cacl_factorial(n-1)

print(cacl_factorial(4))

# cacl_factorial(4)
# = 4 * cacl_factorial(3)
# = 4 *(3 * cacl_factorial(2))
# = 4 * 3 * 2 * cacl_factorial(1)
# = 4 * 3 * 2 * 1 = 24

dir(cacl_factorial)



def cal_add(x,y):
    return x+y


a = 1
type(a)
a = cal_add
type(a)


print(a(1,2))


# anonymous / lambda funtion
# lambda args: expression

aa = lambda x,y: x+y
type(aa)

print(aa(1,200))


aa = lambda x,y: x+y
ab = lambda x,y: x-y
ac = lambda x,y: x*y

def calculator(f, a, b):
    return f(a,b)

calculator(aa, 1, 3)
calculator(ab, 1, 3)
calculator(ac, 1, 3)

# map()
help(map)


list_a = list(range(1,6))
print(list_a)
print(map(lambda x: x**2, list_a))
print(list(map(lambda x: x**2, list_a)))


def cal_add(x):
    return x+1
print(list(map(cal_add, list_a)))

print(list(map(lambda x:x+1, list_a)))

print(list(map(lambda x:x+1, range(1,6))))

# filter
help(filter)

list_b = [1, 3, 5, -3, -9, 100, 1.5]

print(list(filter(lambda x: (x>=0 and x<=6), list_b)))
print(list(filter(lambda x: (type(x) == int), list_b)))
print(list(filter(lambda x: (x % 2 == 1), list_b)))

sol = []
for num in list_b:
    if num % 2 == 1:
        sol.append(num)
print(sol)
