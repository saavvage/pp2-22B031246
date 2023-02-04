#Remove item
#Example remove() , discard()
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#Note: If the item to remove does not exist, remove() will raise an error.
 
#Example discard()
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
""""
Note: If the item to remove does not exist, discard() will NOT raise an error.

You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

The return value of the pop() method is the removed item.
"""
#example pop()
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

#Example clear()
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#example 
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
#The del keyword will delete the set completely:

