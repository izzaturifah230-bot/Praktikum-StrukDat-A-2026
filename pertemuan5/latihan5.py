# 1
stok_barang = [15, 40, 30, 10, 25]

print(stok_barang.index(10))
stok_barang[3] = 50

stok_barang.append(5)
print(stok_barang)
stok_barang.sort()
print(stok_barang)
print(sum(stok_barang))

rata = sum(stok_barang) /len(stok_barang)
print(True) if rata >= 20 else print(False)

# 2
data_aktivitas = [("Diki",88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
for i in range(len(data_aktivitas)) :
    if data_aktivitas[i][1] > 80:
        print(f"{data_aktivitas[i][0]} mendapat peringkat gold ")
    elif 50 <= data_aktivitas[i][1]  <= 80:
        print(f"{data_aktivitas[i][0]} mendapat peringkat silver")
    else  :
        print(f"{data_aktivitas[i][0]} mendapat peringkat bronze")

# 3
ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}

print(ukm_coding - ukm_robotik)
print(ukm_robotik | ukm_coding)
print(True) if 'Andi' in ukm_robotik else print(False)


# 4
gudang_pc = [
{"item": "Monitor", "harga": 1500000, "stok": 5},
{"item": "Keyboard", "harga": 400000, "stok": 12},
{"item": "Mouse", "harga": 250000, "stok": 20}
]

gudang_pc[1]['kategori'] = 'aksesoris'
print(gudang_pc)

gudang_pc.append({"item": "headset",
                  'harga' : 350000,
                   'stok' : 20 })                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
print(gudang_pc)

for i in range(len(gudang_pc)) :
    print(f"Item: {gudang_pc[i]['item']} Total Aset: Rp {gudang_pc[i]['harga']*gudang_pc[i]['stok']}")
