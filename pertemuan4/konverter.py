"""mengubah ke mata uang tetentu"""
import kurs

## dari kusr lain ke idr
def USD_ke_IDR(jumlahAwal) :
    jumlahAkhir = jumlahAwal * kurs.kurses['USD']
    return jumlahAkhir
    
def EUR_ke_IDR(jumlahAwal) :
    jumlahAkhir = jumlahAwal * kurs.kurses['EUR']
    return jumlahAkhir


def SGD_ke_IDR(jumlahAwal) :
    jumlahAkhir = jumlahAwal * kurs.kurses['SGD']
    return jumlahAkhir

def JPY_ke_IDR(jumlahAwal) :
    jumlahAkhir = jumlahAwal * kurs.kurses['JPY']
    return jumlahAkhir

## dari idr ke kurs lain
def IDR_ke_USD(jumlahAwal) :
    jumlahAkhir = jumlahAwal / kurs.kurses['USD']
    return jumlahAkhir

def IDR_ke_EUR(jumlahAwal) :
    jumlahAkhir = jumlahAwal / kurs.kurses['EUR']
    return jumlahAkhir


def IDR_ke_SGD(jumlahAwal) :
    jumlahAkhir = jumlahAwal / kurs.kurses['SGD']
    return jumlahAkhir

def IDR_ke_JPY(jumlahAwal) :
    jumlahAkhir = jumlahAwal / kurs.kurses['JPY']
    return jumlahAkhir
