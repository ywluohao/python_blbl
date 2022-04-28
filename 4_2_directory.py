# os: operating system

# win: "C:\\Program Files (x86)\\Microsoft"
# linux/unix/mac os: "/Users/hao"

# shell: bash zsh fish

import os

os.getcwd()  # get current working directory
print(os.getcwd())

os.getcwd()  # -> "C:\\Program Files (x86)\\Microsoft"
print(os.getcwd())  # -> C:\Program Files (x86)\Microsoft


a = "a\nbc"
a
print(a)

a = "a\\nbc"
print(a)

a = r"a\nbc"  # raw
print(a)

# change directory to
os.chdir("C:\\Program Files (x86)\\Microsoft")  # works
os.chdir("C:\Program Files (x86)\Microsoft")  # fails
os.chdir(r"C:\Program Files (x86)\Microsoft")  # works

os.mkdir("python")

os.chdir("python")
os.getcwd()

os.mkdir("/Users/hao/python/dir1")

os.listdir()
os.listdir("/Users/hao/python/dir1")

os.mkdir("a/b/c")
os.makedirs("a/b/c")

os.listdir("a/b")


os.rename("a", "aa")
os.listdir("aa/b")


os.chdir("dir1")

with open("new.txt", "w") as f:
    f.write("abc")

os.listdir()

os.rename("new.txt", "abc.txt")

os.mkdir("dir2")

os.rmdir("dir2")

os.chdir("..")
os.getcwd()
os.rmdir("dir1")

os.chdir("dir1")
os.remove("abc.txt")

os.chdir("..")

import shutil

dir(shutil)

dir(os)

os.mkdir("d1")
os.chdir("d1")
os.getcwd()
os.listdir()

shutil.copy("new.txt", "../aa")

os.listdir("../aa")

os.chdir("..")
os.rmdir("d1")  # fails
shutil.rmtree("d1")

os.chdir("aa")
shutil.move("new.txt", "b")
shutil.move("bb", "new.txt")

os.listdir("b")

dir(os)
os.curdir

dir(os.path)

os.getcwd()

os.chdir("b")
os.listdir()

os.path.split("/Users/hao/python/aa/b/new.txt")

a = "/Users/hao/python/aa/b/new.txt"
os.path.basename(a)
os.path.dirname(a)

os.path.isfile(a)
os.path.isdir(a)
os.path.isdir("/Users/hao/python/ab")

os.path.join("/Users/hao/python/", "aa")
os.path.join("/Users/hao/python", "aa", "b")

a = os.path.join("/Users/hao/python", "aa", "b1")
if not os.path.isdir(a):
    os.makedirs(a)
os.makedirs(a, exist_ok=True)
