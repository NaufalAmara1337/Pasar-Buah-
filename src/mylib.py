
def inputBuah(nama, stock, harga):
    '''fungsi untuk meminta user input jumlah buah dan menghitung harganya 

    Args:
        nama (string): nama buah yang akan dibeli
        stock (integer): stock buah yang akan dibeli
        harga(integer): harga buah per kg

    returns:
        nBuah (integer): jumlah buah yang dipesan
        hargaBuah (integer): Total harga buah
    '''

    
    #meminta input user
    while True:

        #input jumlah
        nBuah = int(input("Masukan Jumlah {nama}: "))

        #membandingkan antara permintaan dengan stock
        if nBuah > stock:
            print(f'jumlah terlalu banyak, stock tersisa {stock} buah')
            continue

        #jika permintaan terpenuhi maka berhenti minta input
        break

#hitung harga untuk buah tersebut
    hargaBuah = nBuah*harga
    return nBuah, hargaBuah