a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")    #Elif

a = 2
b = 330         # SHORT HAND if...Else
print("A") if a > b else print("B") # One line if else statement:

a = 330
b = 330     # One line if else statement, with 3 conditions:
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:         # and, or, not can also be use
  print("Both conditions are True") 

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

fruits = ["apple", "banana", "cherry"]
for v in fruits:
    print("I like", v)

for i in range(10, 0, -2):
    print(i)

def function_name(parameters):
    # Function's code block
    # ...
    return result  # (optional) return statement to provide a result

def add_numbers(a, b):
    result = a + b
    return result   # Example

# Read on this(What is a function and how do you use functions) extensively later

def greet(name):
    print(f"Hello, {name}!")
    
result = greet("Alice")    # a function that doesn't use a return statement
print(result)  # Output: None

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i]) # iterate over the indices of a sequence, you can combine range() and len()

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number') # Please come back to this task

print("Sammy has {} balloons.".format(5))

