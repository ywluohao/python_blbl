# Python Module, Package, PIP

# Module: file with .py extension

# user-defined module
# Python Standard Library/Module
# other package


### in example.py:

def add(a, b):
    """return the  sum of a and b"""
    result = a + b
    return result

###

### in main.py:

import example

help(example.add)

example.add(1, 2)

###


import math

dir(math)

math.pi

import math as m
m.pi


# method 1
import math
import math as m

# method 2
from math import factorial

factorial(5)
math.factorial(5)


import math
from math import factorial

math.pi
factorial(3)
math.factorial(3)

from math import factorial as f
f(3)


f = 4
f(3)


from math import factorial, pi
pi
factorial(4)
# method 3
from math import *
exp(1)


from math import *
dir()


print('hello')
len([1,2])

import sys
sys.path


# reload module

import imp
imp.reload()



# package:




# numpy, pandas, matplotlib

# directory
# must have __init__.py

import Game.Level.start
Game.Level.start.select_level()

from Game.Level import start
start.select_level()

from Game.Level.start import select_level
select_level()

# PIP
# mac: Terminal
# Win: PowerShell

# Anaconda,

# install, update, uninstall

# tensor flow

import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# PIP
pip3 list
pip3 install numpy
pip3 install numpy --upgrade
pip3 uninstall numpy

pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip3 install -U

pip3 install numpy == 1.17
pip3 install numpy >= 1.17, <2.0
