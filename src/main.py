Apel = int(input("Masukan Jumlah Apel: "))
Jeruk = int(input("Masukan Jumlah Jeruk: "))
Anggur = int(input("Masukan Jumlah Anggur: "))

jumlahApel = 10000
jumlahJeruk = 15000
jumlahAnggur = 100000

tothargaApel = Apel*jumlahApel
tothargaJeruk = Jeruk*jumlahJeruk
tothargaAnggur = Anggur*jumlahAnggur

totBelanja = tothargaApel + tothargaJeruk + tothargaAnggur

print(f"""
Detail Belanja

Apel: {Apel}*{jumlahApel} = {tothargaApel}
Jeruk: {Jeruk}*{jumlahJeruk} = {tothargaJeruk}
Anggur: {Anggur}*{jumlahAnggur} = {tothargaAnggur}
      
Total : {totBelanja}
""")
