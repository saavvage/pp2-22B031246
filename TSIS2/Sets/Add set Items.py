#Add items
#Once a set is created, you cannot change its items, but you can add new items.
#To add one item to a set use the add() method.

#Example  using add()
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Add sets
#To add items from another set into the current set, use the update() method.
#Example 
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Add any itterable 
""""
The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
"""
#Example 
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)