print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#varibel kosong nilainya false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# 0 berarti false
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#fungsi dapat mengengembalikan nilai boolean
def myFunction() :
  return True

print(myFunction())

#bisa mengeksekusi berdasrakan boolean fungsi
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#mengidentifikasi tipe data 
x = 200
print(isinstance(x, int))