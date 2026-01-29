#membelah string
b = "Halo, Dunia!"
print(b[1:4])

#modifikasi string
a = "Halo, Dunia!"
print(a.lower())
a = "Halo, Dunia!"
print(a.upper())

#menghapus spasi dan tab
a = " Halo, Dunia! "
print(a.strip())  # hasilnya "Halo, Dunia!"

#pengubah string
a = "Halo, Dunia!"
print(a.replace("H", "J"))

#membagi string jadi list
a = "Halo, Dunia!"
print(a.split(","))  # hasilnya ['Halo', ' Dunia!']

#menggabungkan string
a = "Halo"
b = "Dunia"
c = a + b
print(c)

age = 21
txt = f"Namaku izza, umurku {age}"
print(txt)


