# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 15

# define a while loop
# while x > 0:
#   print(x)
#   x = x-1

#   y = 0
#   while y < 10:
#     print(y)
#     y = y+1

# define a for loop
months = ["January", "February", "March", "April", "May"]

# use a for loop over a collection
# for m in months:
#   print(m)

# use the break and continue statements
# for m in months:
#   if(m == "April"):
#     break
#   print(m)

for m in months:
  if (m == "March"):
    continue
  print(m)

# using the enumerate() function to get an index and an item
