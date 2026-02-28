
import tabulate
import kurs
import konverter

print("=== KONVERTER MATA UANG ===")

# untuk menampilkan tabel kurs
data = []
for k, v in kurs.kurses.items():
    data.append([k, f"{v:,.0f}".replace(",", ".")])

print(tabulate.tabulate(data, headers=["Kode", "Kurs"], tablefmt="pretty"))

while True :
    while True :
        try :
            mataUangAwal = input('\nDari (IDR/USD/EUR/SGD/JPY):')
            mataUangAkhir = input('Ke (IDR/USD/EUR/SGD/JPY):')
            jumlah = int(input('jumlah: '))
            break
        except ValueError:
            print('masukkan jumlah dan mata uang dengan baik dan benar')


    ##ubah ke IDR
    if mataUangAwal.upper() == 'USD' :
        jumlahIDR = konverter.USD_ke_IDR(jumlah)
        print(f"{jumlah} USD =", end=" ")
    elif mataUangAwal.upper() == 'EUR' :
        jumlahIDR = konverter.EUR_ke_IDR(jumlah)
        print(f"{jumlah} EURO =", end=" ")
    elif mataUangAwal.upper() == 'SGD' :
        jumlahIDR = konverter.SGD_ke_IDR(jumlah)
        print(f"{jumlah} SGD =", end=" ")
    elif mataUangAwal.upper() == 'JPY' :
        jumlahIDR = konverter.JPY_ke_IDR(jumlah)
        print(f"{jumlah} Yen =", end=" ")
    elif mataUangAwal.upper() == 'IDR' :
        print(f"Rp {jumlah} =", end=" ")
        jumlahIDR = jumlah
    else :
        print('mata uang awal nggak valid, ulang lagi')
        continue

    # print(jumlahIDR)

    ## udah dari idr ke kurs lain
    if mataUangAkhir.upper() == 'USD' :
        jumlahKonversi = konverter.IDR_ke_USD(jumlahIDR)
        print(f"{round(jumlahKonversi,2)} USD ")
        break
    elif mataUangAkhir.upper() == 'EUR' :
        jumlahKonversi = konverter.IDR_ke_EUR(jumlahIDR)
        print(f"{round(jumlahKonversi,2)} EURO ")
        break
    elif mataUangAkhir.upper() == 'SGD' :
        jumlahKonversi= konverter.IDR_ke_SGD(jumlahIDR)
        print(f"{round(jumlahKonversi,2)} SGD ")
        break
    elif mataUangAkhir.upper() == 'JPY' :
        jumlahKonversi= konverter.IDR_ke_JPY(jumlahIDR)
        print(f"{round(jumlahKonversi,2)} Yen ")
        break
    elif mataUangAkhir.upper() == 'IDR' :
        jumlahKonversi = jumlahIDR
        print(f"Rp {round(jumlahKonversi,2)}")
        break
    else :
        pass

# print(jumlahKonversi)

