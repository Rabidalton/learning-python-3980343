# LinkedIn Learning Python course by Joe Marini
# Working with modules of code

# import the math module, which contains features for working with mathematics
import math

teams = 32
teampergame = 2

numofgames = math.comb(teams, teampergame)
print(numofgames)

import statistics as s
Ages = [34, 6, 7, 19, 15, 18, 20, 15, 30, 25, 24, 15]

def stats():
  print("Average:", s.mean(Ages))
  print("Mode:", s.mode(Ages))
  print("Median:", s.median(Ages))
  print("Geometric Mean:", s.geometric_mean(Ages))

stats()

# import a specific part of the module so you can refer to it more easily
from statistics import median_low as ml
from statistics import median_high as mh
print("Median Low:", ml(Ages))
print("Median High:", mh(Ages))

# import a module and give it a different name
from fractions import Fraction as frn
print(frn(6, 8))

# the math module contains lots of pre-built functions


# in addition to functions, some modules contain useful constants 


# Generate a random number between 100 and 200
import random as r
print(r.randint(20, 30))

# try some of the math functions for yourself here:

# Use the 3rd party tabulate module to print tabulated data:

# Sample data
data = [
  ["Product", "Price", "Stock"],
  ["Laptop", 999.99, 45],
  ["Mouse", 24.99, 128],
  ["Keyboard", 59.99, 89]
]

# Create a formatted table
from tabulate import tabulate as tb
print(tb(data, headers="firstrow", tablefmt=("fancy_grid")))