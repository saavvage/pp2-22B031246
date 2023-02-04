#Access items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative indexing 
""""
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.

"""
#Example 
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Range of indexes 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
 """"
 Note: The search will start at index 2 (included) and end at index 5 (not included).

Remember that the first item has index 0.

By leaving out the start value, the range will start at the first item:

"""
#Example 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


#Example 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Range of Negative indexes 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if item exists 
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
