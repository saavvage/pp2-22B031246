#Access tuples items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#The first item has index 0.

#Negative Indexing 
#Negative indexing means start from the end.
#-1 refers to the last item, -2 refers to the second last item etc.
#Example 
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Range of indexes
#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new tuple with the specified items.
#example 
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#Note: The search will start at index 2 (included) and end at index 5 (not included).
#Remember that the first item has index 0.

#example 
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#example 
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#range of negative indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#check if item exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")