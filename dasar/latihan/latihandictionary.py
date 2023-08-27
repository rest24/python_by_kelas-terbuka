import datetime
import os
import string
import random

mahasiswa_template = {
    'nama' : '',
    'nim' : '',
    'sks_lulus' : 1,
    'lahir' : datetime.datetime(2001,2,3)   
}

data_mahasiswa = {}

while True :

    os.system("clear")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input ("Nama Mahasiswa : ")
    mahasiswa['nim'] = input ("Nim Mahasiswa : ")
    mahasiswa['sks_lulus'] = int(input ("Sks : "))
    TAHUN_LAHIR = int(input("Tahun Lahir : "))
    BULAN_LAHIR = int(input("Bulan Lahir : "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir : "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
    
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})
    
    print (f"{'KUNCI':<6}{'Nama':<17}{'NIM':<8}{'SKS Lulus':<10}{'Tanggal lahir':<6}")
    print ("-"*50)
    
    for mahasiswa in data_mahasiswa :
        KUNCI = mahasiswa
        NAMA = data_mahasiswa[KUNCI]['nama']
        NIM = data_mahasiswa[KUNCI]['nim']
        SKS = data_mahasiswa[KUNCI]['sks_lulus']
        LAHIR = data_mahasiswa[KUNCI]['lahir'].strftime("%x")
        
        print(f"{KUNCI:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10} ")
        
    print("\n")
    selesai = input ("Sudah beres (y/n) ?")
    if selesai == "y":
        break
        
print ("\nAkhir Program")