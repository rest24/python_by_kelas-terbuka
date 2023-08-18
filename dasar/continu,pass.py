# continue, pass, break

# pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi

# angka = 0
# while angka < 10 :
#    angka +=2
#    if angka == 6 :
#        pass # ini tidak akan dieksekusi
#        print(f"Sekarang adalah angka {angka}")
#    print (f"{angka}.")

# continue 
angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5 :
    angka += 1
    print(f"angka sekarang {angka}") # aksi 1
    if angka == 3:
        print("Nice")
        continue # akan membuat loop meloncat ke step berikutnya
    print("whassup!") # aksi 2
print ("finish!")