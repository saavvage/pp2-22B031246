#Sort List Alphanumerically example

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Example 
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort descending 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Example 
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Customize Sort Function
""""
You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):

"""
#Example
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Case insesitive sort sort()
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
""""
Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function:

"""

#Example 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Reverse order reverse()
""""
What if you want to reverse the order of a list, regardless of the alphabet?

The reverse() method reverses the current sorting order of the elements.

""" 

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
