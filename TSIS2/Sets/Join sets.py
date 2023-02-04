#Join two sets 
""""
There are several ways to join two or more sets in Python.

You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
"""
#Example 
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#Example 
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
#The update() method inserts the items in set2 into set1:
#Note: Both union() and update() will exclude any duplicate items.

#Keep only the duplicates 
#The intersection_update() method will keep only the items that are present in both sets.
#Example 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#The intersection() method will return a new set, that only contains the items that are present in both sets.
#Example 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)


#keep all, but not the Duplicates 
""""
The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
"""
#example 

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)


#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
#example 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

