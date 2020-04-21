# Python namespace and scope

# name (identifier)

a = 100

print(f'a has id {id(a)}')

b = 100

print(f'b has id {id(b)}')

a == b
a is b

c = 99 + 1
print(f'c has id {id(c)}')

# first run: id 4430088064
# second run: id 4319713152

d = 1
print(f'd has id {id(d)}')


list_1 = [1,2,3]
list_2 = [1,2,3]

list_1 == list_2
list_1 is list_2

print(f'list_1 has id {id(list_1)}')
print(f'list_2 has id {id(list_2)}')

a = 100

print(f'a has id {id(a)}')

a += 1 # a = a + 1

print(f'a has id {id(a)}')

list_1.append(4)
list_1
print(f'list_1 has id {id(list_1)}')


# namespace

# built-in: print(), id() ,...
# module: "global"
# funciton: "local"

# variable scope


def outer_fun():
    v1 = 200
    def inner_fun():
        v2 = 300

v3 = 400

# v3 : global

# in inner_fun():

# v3: global
# v2: local
# v1: non-local

def outer_fun():
    a = 20
    def inner_fun():
        a = 30
        print("a= ", a)
    inner_fun()
    print("a= ", a)

a = 10
outer_fun()
print("a= ", a)

# this module - namespace: ... ,a (30) , outer_fun
# outer_fun   - namespace:      a (20) , inner_fun
# inner_fun   - namespace:      a (10) ,


def outer_fun():
    a = 20
    def inner_fun():
        a = 30
        print("a= ", a)
        print(id(a))
    inner_fun()
    print("a= ", a)
    print(id(a))

a = 10
outer_fun()
print("a= ", a)
print(id(a))
