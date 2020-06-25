#Perbedaan Overloading Dan Overriding
#Metode overloading adalah polimorfisme waktu kompilasi. Metode overriding adalah polimorfisme run time.
#Overloading Ini membantu meningkatkan keterbacaan program. Sementara itu overriding digunakan untuk memberikan #implementasi spesifik pada metode yang sudah tersedia oleh class induknya atau kelas super.
#Overloading ini terjadi di dalam kelas. Sementara itu overriding dilakukan dalam dua kelas dengan hubungan #warisan.Overloading ini terjadi di dalam kelas. Sementara itu overriding dilakukan dalam dua kelas dengan hubungan warisan.
#Metode overloading mungkin atau mungkin tidak memerlukan pewarisan. Sementara metode override selalu membutuhkan pewarisan.


class Bapak(object):
    def __init__(self, nama, tinggi, berat):
        self.nama = nama
        self.tinggi = tinggi
        self.berat = berat

    def berjalan(self):
        print("Berjalan ke tenang")

    def berlari(self):
        print("Berlari dengan cepat")


# class Anak turunan dari class Bapak
class Anak(Bapak):
    # class anak melakukan overide terhadap method berlari
    def berlari(self):
        print("Berlari masih tertatih-tatih")

    # class anak memanggil method berlari yang ada di class bapak
    def berlari_baseclass(self):
        return super(Anak, self).berlari()

    # method yang hanya dimiliki class anak
    def menangis(self):
        print("Menangis dengan keras")


b = Bapak("Wiragan", 170, 68)
print("Nama:", b.nama)
print("Tinggi:", b.tinggi, "cm")
print("Berat:", b.berat, "kg")
b.berjalan()
b.berlari()

# objek dari class Anak memiliki seluruh yang dimiliki class Bapak
a = Anak("Mustofa", 140, 32)
print()
print("Nama:", a.nama)
print("Tinggi:", a.tinggi, "cm")
print("Berat:", a.berat, "kg")
a.berjalan()
a.berlari()
a.berlari_baseclass()
a.menangis()