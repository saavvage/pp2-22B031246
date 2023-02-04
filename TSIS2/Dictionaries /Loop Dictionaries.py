#Loop through a Dictionary
""""
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
"""
#Example 
for x in thisdict:
  print(x)
  
#Example 
for x in thisdict:
 print(thisdict[x])
  
#Example values()
for x in thisdict.values():
  print(x)
  
#Example keys()
for x in thisdict.keys():
  print(x)

#Example items()
for x, y in thisdict.items():
  print(x, y)
  
  
 