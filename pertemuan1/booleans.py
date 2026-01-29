print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b lebih besar dari a")
else:
  print("b tidak lebih besar dari a")

# variabel kosong dianggap false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# nilai 0 berarti false
class MyClass():
  def __len__(self):
    return 0

objek = MyClass()
print(bool(objek))

# fungsi bisa mengembalikan nilai boolean
def cekNilai():
  return True

print(cekNilai())

# bisa mengeksekusi kode berdasarkan hasil boolean dari fungsi
def cekNilai():
  return True

if cekNilai():
  print("YA")
else:
  print("TIDAK")

# mengecek tipe data
x = 200
print(isinstance(x, int))
