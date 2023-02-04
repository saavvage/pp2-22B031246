#Change item value example 
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change a range of item values
""""
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
""""
If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

"""

#Example 
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
""""
Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

"""
#Example 
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


#Insert items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)