import os

os.getcwd()
os.listdir()


f = open(
    "aa.txt",
)

# mode:
# 'r': read
# 'w': write // truncate
# 'a': append
# 'x': exclusive write

# '+': read and write
# 'r+': read and write
# 'w+': truncate and read
# 'rw': wrong


f.read()
f.readline()
f.readlines()

f.write()
f.writelines()

f = open("a1.txt", "w")
f.readable()
f.writable()

f.read()

f.write("1234567890\n" * 10)
f.close()


f = open("a1.txt", "r")
f.readable()
f.writable()
f.read()
f.close()


f = open("a1.txt", "r")
f.read()
f.close()


with open("a1.txt", "r") as f:
    f.read()

f.closed


f = open("a1.txt", "r")
f.read(1)
f.read(15)
f.read()

f.readline()

f.readlines()


f.tell()
f.seek(5)

f = open("a1.txt", "w")
f.writelines(["abcd\n", "efg"])

f = open("a1.txt", "a")
f.writelines(["abcd\n", "efg"])

f = open("aw.txt", "x")

for i in range(1, 4):
    with open(f"a{i}.txt", "w") as f:
        f.writelines(["abcd\n", "efg"])

os.listdir()

dir(os.path)
for i in range(1, 4):
    print(f"a{i}.txt", os.path.getsize(f"a{i}.txt"))

d = {}

d["r+"] = open("a1.txt", "r+")
d["w+"] = open("a2.txt", "w+")
d["a+"] = open("a3.txt", "a+")

for k, v in d.items():
    print(k, v.tell(), v.write("123"), v.tell())
    # print(v.readable())
    # print(v.writable())


with open("aa.txt", "r") as f:
    for line in f.readlines():
        print(line.strip())

dir(str)


with open("aa.txt", "r") as f:
    for line in f:
        print(line.strip())
