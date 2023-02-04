#Python dictionaries 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#Dictionary
""""
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:
"""
#Example 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Dictionary items 
#Dictionary items are ordered, changeable, and does not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

#Example 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])


#Ordered or Unordered?
""""
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
"""
#Duplicates not allowed
#Dictionaries cannot have two items with the same key:
#Example 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#Dictionary length len()
#Example 
print(len(thisdict))


#Dicrionary items - Data Types
#The values in dictionary items can be of any data type:
#Example 

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#type()
""""
From Python's perspective, dictionaries are defined as objects with the data type 'dict':

<class 'dict'>
    """
#example 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))


#The dict() constructor 
#It is also possible to use the dict() constructor to make a dictionary.
#Example 
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


#python collection (arrays)
""""
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
"""


    