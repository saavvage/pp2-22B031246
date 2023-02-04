#remove specified item example 
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Example 
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#Example 
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Example 
thislist = ["apple", "banana", "cherry"]
del thislist

#Clear the list example 
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
