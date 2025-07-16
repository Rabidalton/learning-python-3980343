# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionary: a key-value data structure
myDict = {
  "Name" : "Dalton",
  "Age": 25, 
  "Address": "Cooper Farm",
  "School": "CMU-Africa",
  "Tel": "+231886501849"
}

print(myDict)

# dictionaries are accessed via keys
print(myDict["Address"])
print(myDict["Age"])

# you can also set dictionary data by creating a new key
myDict["Address"] = "Kigali"
print(myDict)

# Trying to access a nonexistent key will produce an error
print(myDict["Num"])

# To avoid this, you can use the "in" operator to see if a key exists
print("Address" in myDict)
print("Num" in myDict)

# You can retrieve all of the keys and values from a dictionary
print(myDict.keys())
print(myDict.values())

# You can also iterate over all the items in a dictionary
for key, val in myDict.items():
  print(key, val)