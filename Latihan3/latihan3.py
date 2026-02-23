class Person :
    def __init__(self, nama, jenisKelamin, umur):
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.umur = umur

class Karyawan(Person) :
    def __init__(self, nama, jenisKelamin, umur, gaji):
        super().__init__(nama, jenisKelamin, umur)
        self._gaji = gaji

    def get_gaji(self):
        return self._gaji
    
    def set_gaji(self, gajiBaru):
        self._gaji = gajiBaru
    
    
class Rekening :
    def __init__(self, noRek, PIN):
        self.noRek = noRek
        self.__PIN = PIN
    
    def get_PIN(self):
        return self.__PIN
    
    def set_PIN(self, pinBaru):
        self.__PIN = pinBaru

p1 = Karyawan("oliv", "perempuan", 20, 100000)
r1 = Rekening("123", "1111")

print(r1.get_PIN())
print(p1.nama)
print(p1.get_gaji())



