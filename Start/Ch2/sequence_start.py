# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [1, 6, 15, "Dalton", "John", 3, 10]


# to access a member of a sequence type, use []
# print(mylist)
# print(mylist[0])
# print(mylist[4])

# add a list to another list
# myNewList = [24, "Darius"]
# myNewList = print(myNewList + mylist)

# mylist[1] = "3"
# print(mylist)

# use slices to get parts of a sequence
# print(mylist[1:5])
# print(mylist[3:6:2])
# print(mylist[::2])

# you can use slices to reverse a sequence
# print(mylist[::-1])

# Tuples are like lists, but they are immutable
myTuples = (2, 4, 6, 8, 10)
# print(myTuples)
# print(myTuples[2])
# myTuples[3] = 11

# Sets are also sequences, but they contain unique values
mySet = {3, 5, 7, 9, 3, 7, 9, 10, 9}
# print(mySet)
# print(mySet[3])
# Set, however, can not be indexed like lists or tuples

# print(myset[0]) # this will cause an error
# print(mySet[0])

# Test for membership
print(3 in mylist)
print("Dalton" in mylist)
print(6 in myTuples)
print(44 in mySet)