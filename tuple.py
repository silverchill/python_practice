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