import mylib

print("selamat datang di pasar buah mang dadang")

#definisikan stock buah
stockApel = 10
stockJeruk = 8
stockAnggur = 15

#definisikan harga buah
hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000

#meminta input jumlah buah apel
nApel, totalhargaApel = mylib.inputBuah(nama="Apel", stock=stockApel, harga=hargaApel)
nJeruk, totalhargaJeruk = mylib.inputBuah(nama="Jeruk", stock=stockJeruk, harga=hargaJeruk)
nAnggur, totalhargaAnggur = mylib.inputBuah(nama="Anggur", stock=stockAnggur, harga=hargaAnggur)

#menghitung total belanja
totBelanja = totalhargaApel + totalhargaJeruk + totalhargaAnggur

#tampilkan rincian belanjaan 
print(f"""
Detail Belanja

Apel: {nApel}*{hargaApel} = {totalhargaApel}
Jeruk: {nJeruk}*{hargaJeruk} = {totalhargaJeruk}
Anggur: {nAnggur}*{hargaAnggur} = {totalhargaAnggur}
      
Total : {totBelanja}
""")

#proses pembayaran
while True:
    #input jumlah uang
    bayar = int(input('silahkan masukan uang anda: '))
    
    #hitung Selisih antara bayar dengan total
    selisih = totBelanja - bayar
    
    #bandingkan antara uang dan total harga
    if bayar > 0:
        print(f"uang anda kurang sebesar Rp.{selisih}")
        continue
   #ucapkan terimakasih ketika selesai transaksi
    else: 
        print(f"""Terima kasih Uang kembalian anda: {abs(selisih)}""")
        break