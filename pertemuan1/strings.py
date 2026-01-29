#membelah string
b = "Hello, World!"
print(b[2:5])

#modifikasi string
a = "Hello, World!"
print(a.lower())
a = "Hello, World!"
print(a.upper())

#menghapus spasi dan tab
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#pengubah string
a = "Hello, World!"
print(a.replace("H", "J"))

#membagi string jadi list
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#menggabungkan string
a = "Hello"
b = "World"
c = a + b
print(c)

age = 36
txt = f"My name is John, I am {age}"
print(txt)

