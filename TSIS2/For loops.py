#Python for loops
""""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

"""

#Example 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
  
  #Looping Through string
  for x in "banana":
  print(x)
  
  #The break Statement 
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Example 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#The continue statement 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
  
  #The range function 
  """"
  To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

"""

for x in range(6):
  print(x)
  
  """"
  Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

"""
#Example 
for x in range(2, 6):
  print(x)
  
  #Example 
for x in range(2, 30, 3):
  print(x)
  
  #Else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
  """"
Note: The else block will NOT be executed if the loop is stopped by a break statement.

"""
#Example 

  for x in range(6):
if x == 3: break
  print(x)
else:
  print("Finally finished!")
  
  #Nested loop
  adj = ["red", "big", "tasty"]
  fruits = ["apple", "banana", "cherry"]

  for x in adj:
   for y in fruits:
    print(x, y)
    
    #The pass statement
    """"
    for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

"""
    for x in [0, 1, 2]:
     pass