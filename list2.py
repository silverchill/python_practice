house = ["chair", "table", "tv"]
new_home = []
for r in house:
    if "a" in r:
        new_home.append(r)
print(new_home)         # To create a new list from the values of former list using for loop

house = ["chair", "table", "tv"]
new_home = [r for r in house if "a" in r]
print(new_home)         #list compression help us to do this loop in a short format
            #THE SYNTAX   newlist = [item 'for' item 'in' oldlist if condition == True]

house = ["chair", "table", "tv"]
new_home = ["car" for r in house]
print(new_home)         #To replace all value in the new home to car

house = ["chair", "table", "tv"]
new_home = [r if r != "chair" else "cup" for r in house]
print(new_home)         # To replace chair with cup in the new list

house = ["chair", "table", "tv"]
new_home.sort(reverse = True)
print(new_home)         # To sort a list in descending order

def myfunc(n):
  return abs(n - 300)
y = [200, 500, 650, 50, 10]
y.sort(key = myfunc)
print(y)            # To sort a no on how close it is to a no

