t = "beautiful"

def mysch():
    print(" The school is " + t)
mysch()                          #global variable declaration

def mysch():
    global y
    y = "good"
mysch()
print("The boy is " + y)    #global variable declared in a fxn(done using global keyword)

u = "coming"

def mysch():
    global u
    u = "girl"
mysch()
print("she's a good " + u) #Using a global keyword to change the value of a global variable inside a fxn
