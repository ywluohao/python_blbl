# Python global, local

# built-in:
# module:  global
# function: local

# global variable vs local variable

x1 = 1
def a_fun():
    x1 = 2
    print("inside", x1)
a_fun()
print("outside", x1)

# inside a function: local > global


x1 = 1
def a_fun():
    # x1 = 2
    print("inside", x1)
a_fun()
print("outside", x1)

# we can access global variables INSIDE a function.

x1 = 1
def a_fun():
    x1 += 1
    print("inside", x1)
a_fun()
print("outside", x1)

# x1 = x1 + 1

# update local
x1 = 1
def a_fun():
    x1 = 200
    x1 += 1
    print("inside", x1)
a_fun()
print("outside", x1)


# update global
x1 = 1
def a_fun():
    global x1
    x1 += 1
    print("inside", x1)
a_fun()
print("outside", x1)


# local, no global
def b_fun():
    y1 = 'local'

b_fun()
print(y1)



def b_fun():
    y1 = 'local'
    print(y1)

b_fun()


a = 'global'
def foo():
    global a
    b = 'local'
    a *= 2
    print(a)
    print(b)

foo()
print(a)
print(b)




t1 = 100
def outer():
    t1 = 200
    def inner():
        t1 = 300
        print("inner",t1)
    inner()
    print("outer",t1)
outer()
print("global",t1)


t1 = 100
def outer():
    t1 = 200
    def inner():
        global t1
        t1 += 1
        print("inner",t1)
    inner()
    print("outer",t1)
outer()
print("global",t1)


t1 = 100
def outer():
    t1 = 200
    def inner():
        nonlocal t1
        t1 += 1
        print("inner",t1)
    inner()
    print("outer",t1)
outer()
print("global",t1)

# nested function:
# global keyword works on outmost level
# nonlocal keyword works on one level up


def foo():
    x = 20
    def bar():
        global x
        x = 30
        print("bar:", x)
    bar()
    print("foo", x)
foo()
print("main", x)
