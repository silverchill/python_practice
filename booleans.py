bool("abc"), bool(123), bool(["apple", "cherry", "banana"]) # They are all True

"""
there are not many values that evaluate to False, except empty values, such as
bool(False), (None), (0), (""), (()), ([]), ({}) This are only false statement
Also an object that is made from a class with a __len__ function that returns 0 or False
"""
def myFunction():
  return 1

if myFunction():
  print("YES!")
else:
  print("NO!")  #if true(1) print YES but if false(0) print NO
'''
The 4 built-in data types in Python used to store collections of data

List: is a collection which is ordered and changeable. Allows duplicate members.
Tuple: is a collection which is ordered and unchangeable. Allows duplicate members.
Set: is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary: is a collection which is ordered** and changeable. No duplicate members.
'''
# mylist = ["Ste", "Solo", "Chi"] or mylist = list(("Ste", "Solo", "Chi")) both are list data types

x = ["Ste", "Solo", "Chi"]
print(type(x))

x = list(("Ste", "Solo", "Chi"))
print(type(x))
