value = ["Apple", "Egg", "Castle"]
value[1] = "bag"
print(value)       #To change the value of a specific item, refer to the index no

g = ["Water", "Bread", "Dog", "Cow"]
g.insert(3, "cat")
print(g)        #To add an object at a specific index in the list, use "insert"

g = ["Water", "Bread", "Dog", "Cow"]
g.append("cat")
print(g)        # To add an object at the end of a list, use "append"

g = ["Water", "Bread", "Dog", "Cow"]
h = ["age", "boy", "has"]
g.extend(h)
print(g)    # To add a (list, tuples, sets, dictionaries etc) to another list, use "extend"

i = ["Water", "Bread", "Dog", "Cow"]
i.remove("Dog")
print(i)    # To remove an item in a list, use "remove"

i = ["Water", "Bread", "Dog", "Cow"]
i.pop(2)       # To remove a specific index in a list, use "pop" or
del i[0]        # To remove a specific index in a list, use "del"
print(i)       # To remove the entire list, use "del with specifying any index eg "del i" "

i = ["Water", "Bread", "Dog", "Cow"]
i.pop()
print(i)     #To remove the last index in a list, use "pop"without adding any specific index no

i = ["Water", "Bread", "Dog", "Cow"]
i.clear()
print(i)    #To clear all the content in a list while keeping the list ie empty list

the = ["come", "here"]
for r in the:
    print(r)                      # To loop through a list using for loop

the = ["dont", "relax"]
[print(r) for r in the]          # To loop through a list using for loop

St = ["Yam", "stew"]
for r in range(len(St)):
    print(St[r])                # To loop through a list using for loop

St = ["Yam", "good"]
for r in range(len(St)):
    print([r])                # To loop through the index in a list using for loop

egg = ["bread", "akara"]
f = 0
while f < len(egg):
    print(egg[f])               # NB: f += 1 is the same as f = f + 1
    f += 1                      # To loop through a list using while loop


