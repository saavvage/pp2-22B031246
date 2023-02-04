#Append items append()
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert items insert()
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Extend list 
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Add any iterable extend()
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

