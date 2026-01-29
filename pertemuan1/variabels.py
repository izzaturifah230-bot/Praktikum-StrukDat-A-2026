x = 5
y = "Izza"
print(x)
print(y)

x = 4        # x bertipe integer
x = "Izza"   # x sekarang bertipe string
print(x)

# casting (konversi tipe data)
x = str(3)     # x menjadi '3'
y = int(3)     # y menjadi 3
z = float(3)   # z menjadi 3.0

# melihat tipe data
x = 5
y = "Izza"
print(type(x))
print(type(y))

# tanda " dan ' itu sama
x = "Izza"
# sama dengan
x = 'Izza'

# Python sensitif terhadap huruf besar dan kecil
a = 4
A = "Izza"    # a dan A adalah variabel yang berbeda

# contoh nama variabel yang benar
nama = "Izza"
nama_user = "Izza"
_nama = "Izza"
namaUser = "Izza"
NAMA = "Izza"
nama2 = "Izza"

# memasukkan banyak nilai sekaligus
x, y, z = "Izza", "Izza", "Izza"
print(x)
print(y)
print(z)

buah = ["Izza", "Izza", "Izza"]
x, y, z = buah
print(x)
print(y)
print(z)

# output variabel
x = "bahasa"
print(x)

x = "Python"
y = "itu"
z = "Izza"
print(x, y, z)

x = "Python "
y = "itu "
z = "Izza"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "Izza"
print(x, y)

# variabel global
x = "Izza"

def myfunc():
    print("Python " + x)

myfunc()

x = "Izza"

def myfunc():
    x = "Izza"
    print("Python" + x)

myfunc()

print("Python " + x)
