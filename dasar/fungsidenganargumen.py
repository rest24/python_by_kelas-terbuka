'''fungsi dengan argument (input)'''

'''def nama_fungsi(argument):
    badan fungsi'''
    
def hello_word(nami):
    '''fungsi hello word menerima inut dengan variable nami'''
    print(f"Selamat datanga dunia wahai {nami}")
    
hello_word("ujang")
hello_word("dadang")

# program tambah

def tambah (angka_1,angka_2):
    '''fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")
    
tambah(3,6)
tambah(7,43)

def say_hi(daftar_peserta):
    '''fungsi say_hi'''
#    daftar_peserta[1]= "Asep" # mengcopy/duplikat juga yang luar
    data_peserta = daftar_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")
anggota = ["Ucup","Otong","Dudung"]

say_hi(anggota) 

# print(anggota[1]) # duplikat yang anggota