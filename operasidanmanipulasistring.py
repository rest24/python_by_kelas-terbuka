# operasi dan manipulasi string

# 1. Menyambung string (contatenate)
nama_pertama = "Restu"
nama_tengah = "Andryana"
nama_akhir = "Suhendar"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print("Panjang dari nama lengkap" + nama_lengkap + "=" + str(panjang))

# 3. Operator untuk string

# mengecek apakah ada komponen char atau string di string 
d = "d"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))
D = "D"
status = D in nama_lengkap
print("string " + D + " ada di " + nama_lengkap + " = " + str(status))
d = "d"
status = d not in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(20*"wk")

# indexing
print("Index ke-0 : " + nama_lengkap[0])
print("Index ke-20 : " + nama_lengkap[20])
print("Index ke-(-5) : " + nama_lengkap[-5])
print("Index ke-(-7) : " + nama_lengkap[-7])
print("Index ke-[0:5] : " + nama_lengkap[0:5])
print("Index ke-[6:14] : " + nama_lengkap[6:14])
print("Index ke-[0,2,4,6,8,10] : " + nama_lengkap[0:10:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling kecil : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII untuk spasi adalah " + str(ascii_code))
data = 117
print("ASCII untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada" + data + " = " + str(jumlah))