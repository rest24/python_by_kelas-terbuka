# latihan perulangan membuat segitiga 

sisi = 25

# 1. Menggunakan For
# dummy variable 
print("Awal dari for")
count = 1
for i in range (sisi):
    print("*"*count)
    count += 1
print("Akhir dari for")

# 2. Menggunakan while
print("Awal while")
count = 1
while True :
    print("*"*count)
    count += 1
    
    if count > sisi :
        break
print("Akhir while")

# 3. Hanya ganjil saja
print("Awal while")
count = 1
while True :
    if (count%2):
        # print jika ganjil
        print("*"*count)
        count += 1
    else:
        # akan kembali keatas jika ganjil
        count += 1
        continue
    
    # akan break jika count melebihi sisi    
    if count > sisi :
        break
print("Akhir while")

# 4. Hanya ganjil saja
print("Awal while")
count = 1
spasi = int(sisi/2)
while True :
    if (count%2):
        # print jika ganjil
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali keatas jika ganjil
        count += 1
        continue
    
    # akan break jika count melebihi sisi    
    if count > sisi :
        break
print("Akhir while")
