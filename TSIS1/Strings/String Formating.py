#String Format
#Example 
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

#Example 
txt = "The price is {:.2f} dollars"

#Multiple values Example
print(txt.format(price, itemno, count))

#Example
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#Index Numbers Example
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#Example
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))


#Name Indexes Example
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

