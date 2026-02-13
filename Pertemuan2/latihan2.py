
nilai = [75, 80, 65, 90, 85]

#Tambahkan nilai 95 ke dalam list.
nilai.append(95)
print(nilai)

#Urutkan list dari nilai terkecil ke terbesar.
nilai.sort()
print(nilai)

# Hapus nilai terendah dari list.
nilai.pop(0)
print(nilai)


print(nilai)

print(nilai[len(nilai)-1])
print(nilai[0])


jumlah = 0
for i in nilai :
    jumlah += i

rata = jumlah / (len(nilai))

# Tampilkan seluruh isi list setelah diproses.
print(nilai)
print(rata)

#2 tuple
dosen = ("D001", "Dr. Andi", "Struktur Data", 12)

# Tampilkan nama dosen dan mata kuliah yang diampu.
print(dosen[1])
print(dosen[2])

# Tampilkan seluruh isi tuple menggunakan perulangan
for i in dosen :
    print(dosen)


#Coba ubah jumlah SKS menjadi 14, lalu jelaskan apa yang terjadi.
# dosen[3] = 14

"""kelebihan tupple adaslah, nilainya konsten, jadi kita nggak khawatir isinya berubah"""

#Coba ubah jumlah SKS menjadi 14, lalu jelaskan apa yang terjadi.

#3
keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}

print(keahlian_A.intersection(keahlian_B))
print(keahlian_A.difference(keahlian_B))

#keahlian unik
unik = []
unik.append = print(keahlian_A.difference(keahlian_B))
unik.append = print(keahlian_B.difference(keahlian_A))

print(unik)

# benar = is "java" in keahlian_B

unik.append = print(keahlian_A.difference(keahlian_B))

unik.append = print(keahlian_A.difference(keahlian_B))

#4





