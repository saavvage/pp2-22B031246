#Boolean Values Example
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Example
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
  
  #Evaluate Values and Variables Example
  print(bool("Hello"))
print(bool(15))

#Example
x = "Hello"
y = 15

print(bool(x))
print(bool(y))


#Most values are True Example
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


#Some values are false Example
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


#example 
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
 
 
 #function can return a boolean Example
 def myFunction() :
  return True

print(myFunction())

#Example
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
  #Example
x = 200
print(isinstance(x, int))
 