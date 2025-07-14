# LinkedIn Learning Python course by Joe Marini
# Example file for variables and basic types


# Basic data types in Python: Numbers, Strings, Booleans 
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 
myint = 10
myfloat = 13.2576
mystr = "This is a string"
mybool = True

# We can display the content of a variable using the print() function
# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)


# Operators are used to perform operations on variables
print(myint + myfloat)
print(mybool >= myfloat)
print(myfloat == 10)
print(myint < 24)
# Logical and comparison operators 
print(myfloat < 15 or myint >= 20)

# re-declaring a variable works
myint = 30
print(myint)