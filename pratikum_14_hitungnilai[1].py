#Mengimput nama,nim dan nilai
nama=raw_input("Masukkan Nama 					: irha")
nim=input("Masukkan NIM                   : 126")
uts=input("Masukkan Nilai UTS             : 90")
uas=input("Masukkan Nilai UAS             : 88")
tugas=input("Masukkan Nilai Tugas           : 85" )

Uts=uts*40/100;
Uas=uas*40/100;
Tugas=tugas*20/100;
#Formula mencari nilai akhir
nilai_akhir=Uts+Uas+Tugas;

#Menampilkan ouput nama, Nim dan Nilai yang telah diinput
print "\nNama			    :%s" % nama
print "NIM 		        :%s" %nim
print "Nilai UTS		:%d" %uts
print "Nilai UAS 		:%d" %uas
print "Nilai Tugas  	:%d" %tugas
print "Nilai Akhir		:" ,float(nilai_akhir)

#kondisi if untuk menentukan nilai huruf
if nilai_akhir >=80 :
	print "\nNilai Huruf  : A"
elif nilai_akhir >=70 :
	print "\nNilai Huruf  : B"
elif nilai_akhir >=55 :
	print "\nNilai Huruf  : C"
elif nilai_akhir >=40 :
	print "\nNilai Huruf  : D"
elif nilai_akhir <=39 :
	print "\nNilai Huruf  : E"

#kondisi if untuk menentukan keterangan LULUS atau TIDAK LULUS
if nilai_akhir >=60 :
	print "keterangan    : LULUS"
else :
	print "keterangan    : TIDAK LULUS"

