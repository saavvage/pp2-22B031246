#Strings example
print("Hello")
print('Hello')

#Assign String to a Variable example
a = "Hello"
print(a)

#Multiline string example
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

 #example tree singlie votes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings and arrays example
a = "Hello, World!"
print(a[1])

#Looping through string example
for x in "banana":
  print(x)
  
  #String length example 
a = "Hello, World!"
print(len(a))
  
#Check string example 
txt = "The best things in life are free!"
print("free" in txt)

#example
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if not example
txt = "The best things in life are free!"
print("expensive" not in txt)

#example
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")