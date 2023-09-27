x = "Hello World"
print(type(x)) #To get the type of data use type()

x = 1j
print(type(x)) #complex data type

x = ("Steve", "Solo", "Chi")
print(type(x))     #tuple data type

x = ["Steve", "Solo", "Chi"]
print(type(x))    #list data type

x = range(7)
print(type(x))      #range data type

x = {"apple", "banana", "cherry"}
print(type(x))      #set data type

x = {"apple" : "banana", "cherry" : 50}
print(type(x))      #dict data type

x = b"Steve"
print(type(x))      #bytes data type

x = False
print(type(x)) #bool data type NB: T or F should be in capital

b = """This a way to assign,
long string like a sentence"""
print(b)

for w in "Steve":
    print(w)        #for loop, To print each character in a way

e = "Hello, Stephen"
print(len(e))       #To count the no of character in a string(return length of string)

cat = "We are good together"
print("hat" not in cat) #To check if a word is in a sentence, we use 'in or not' to get true or false

txt = "The best things in life are free!"
if "freed" in txt:
  print("Yes, 'freed' is present.")
else:
    print("No, 'freed' is absent.") #Using if and else statement

r = "Stephen, Egwuatu"
print(r[2:6])   #Get the characters from position 2 to position 6(not included)

y = "Stephen, Egwuatu"
print(y[:6])    #Get the characters from the start to position 6(not included)

z = "Stephen, Egwuatu"
print(z[3:]) #Get the characters from position 2, and all the way to the end

c = "stella"
print(c.upper()) #To return a string in upper case use upper()

f = "steve, "
print(f.strip()) #To return string without the whitespace

d = "Hello, World!"
print(d.replace("Hello", "Ste")) #To replace a string or character

g = "Obi is a boy!"
print(g.split(" ")) #To return another string