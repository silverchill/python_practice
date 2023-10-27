"""
Tuples are used to store multiple items in a single variable, A tuple is a collection which is ordered and
unchangeable. Tuples are written with round brackets
"""

thistuple = ("apple", "banana", "cherry") # This is a tuple
print(thistuple)

thistuple = tuple(("apple", "banana", "cherry")) # This is also a tuple
print(thistuple)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(*red,) = fruits
print(red) # adding * to the variable name will make the rest values come as a list

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)    # True and 1 are consider to be same value in set

thisset = set(("apple", "banana", "cherry"))
print(thisset)      # This is also a tuple

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)      # Using 'add' to add orange to the set

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)      # update() method inserts the items in set2 into set1

# use .clear(Name_of_set) to get an empty set
# NB Both union() and update() will exclude any duplicate items

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)      # The "union()" method returns a new set with all items from both sets

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)    # To print the item present in both set

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)    # To remove all duplicates in a set

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(type(thisdict))       # THIS IS A DICTIONARY

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)             # THIS IS ALSO A DICTIONARY

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisdict["model"]
print(x)

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisdict.get("model")  # Both will give you Mustang
print(x)

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisdict.keys()
print(x)    # keys() method will return a list of all the keys in the dictionary

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisdict.values()
print(x)    # values() method will return a list of all the values in the dictionary

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.keys()
print(x)                # before the change
car["color"] = "white"
print(x)                # after the change

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.values()
print(x)                # before the change
car["color"] = "red"
print(x)                # after the change

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisdict.items()
print(x)      # items() method will return each item in a dictionary, as tuples in a list




