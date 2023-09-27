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