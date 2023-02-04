#Python loops
""""
while loops
for loops
"""

#The wile loop example
i = 1
while i < 6:
  print(i)
  i += 1
  
  #The break Statement example 
  i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#The continious statement example 
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
  #The else statement example 
  i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
