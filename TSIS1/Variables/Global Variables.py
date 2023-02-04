#example 
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#example 
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


#The global keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


#example x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



