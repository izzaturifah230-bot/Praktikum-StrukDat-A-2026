x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#melihat tipe data 
x = 5
y = "John"
print(type(x))
print(type(y))

# " dan ' sama
x = "John"
# is the same as
x = 'john'

#python itu bahsa yang sensitif dngn case
a = 4
A = "Sally" #merupakan 2 bariabel berbeda

#nama variabel yang benar
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#bisa memasukkan banyak nilai
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#output variabel
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

#variabel global
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"


def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

