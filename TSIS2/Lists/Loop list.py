#Loop through the list (for)
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
  #Loo through the index number range() len()
  thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
  #Using a whiel loop 
  """"
  You can loop through the list items by using a while loop.

Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

Remember to increase the index by 1 after each iteration.

"""
#Example 
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
  #Looping using list comprehension
  
  thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
