# program list buku
daftar_buku = []
while True :
    print("masukkan buku")
    judul = input("judul buku\t : ")
    penulis = input("nama penulis\t : ")

    buku_baru = [judul,penulis]
    daftar_buku.append(buku_baru)

    print("\n\n","="*10,"Data buku","="*10)
    for index,buku in enumerate(daftar_buku) :
        print(f" {index+1} | {buku[0]} | {buku[1]} ")
    
    print("\n\n","="*20)
    lanjut = input("Apakah lanjut? (y/n) ")
    
    if lanjut == "n" :
        break
    
print("Program selesai")