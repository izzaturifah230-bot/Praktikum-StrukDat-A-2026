# tipe data angka
x = 7      # int
y = 5.6    # float
z = 2j     # 
print(type(x))
print(type(y))
print(type(z))

x = 7      # int
y = 5.6    # float
z = 2j     # complex

# konversi dari int ke float
a = float(x)

# konversi dari float ke int
b = int(y)

# konversi dari int ke complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# bisa import angka random
import random

print(random.randrange(5, 15))
