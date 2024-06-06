print("selamat datang di pasar buah mang dadang")

#definisikan stock buah
stockApel = 10
stockJeruk = 8
stockAnggur = 15

#definisikan harga buah
jumlahApel = 10000
jumlahJeruk = 15000
jumlahAnggur = 20000

#meminta input user
while True:
    #input jumlah
    Apel = int(input("Masukan Jumlah Apel: "))
    #membandingkan antara permintaan dengan stock
    if Apel > stockApel:
        print(f'jumlah terlalu banyak, stock tersisa {stockApel} buah')
        continue
    #jika permintaan terpenuhi maka berhenti minta input
    break

#meminta input user
while True:
    #input jumlah
    Jeruk = int(input("Masukan Jumlah Jeruk: "))
    #membandingkan antara permintaan dengan stock
    if Jeruk > stockJeruk:
        print(f'jumlah terlalu banyak, stock tersisa {stockJeruk} buah')
        continue
    #jika permintaan terpenuhi maka berhenti minta input
    break

#meminta input user
while True:
    #input jumlah
    Anggur = int(input("Masukan Jumlah Anggur: "))
    #membandingkan antara permintaan dengan stock
    if Anggur > stockAnggur:
        print(f'jumlah terlalu banyak, stock tersisa {stockAnggur} buah')
        continue
    #jika permintaan terpenuhi maka berhenti minta input
    break

#menghitung total belanja
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

#proses pembayaran
while True:
    #input jumlah uang
    bayar = int(input('silahkan masukan uang anda: '))
    
    #hitung Selisih antara bayar dengan total
    selisih = totBelanja - bayar
    
    #bandingkan antara uang dan total harga
    if bayar > 0:
        print("uang anda kurang sebesar Rp.{selisih}")
        continue
   #ucapkan terimakasih ketika selesai transaksi
    else: 
        print(f"""Terima kasih Uang kembalian anda: {abs(selisih)}""")
        break