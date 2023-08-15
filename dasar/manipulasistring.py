# operator dalam bentuk methods

## mengubah case dari string 

# merubah semua ke upper case

salam = "bro!"
print ("Normal = " + salam)
salam = salam.upper()
print ("Upper = " + salam)

# merubah semua ke lower case
alay = "Aku kEcE AbiiIEZzz"
print("normal = " + alay)
alay = alay.lower()
print ("Lower = " + alay)

## pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print (salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()
print (salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf 
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline \n 
# istitle() <-- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasil bool
print (judul + " is title = " + str(cek_judul))

## ngecek komponen startswith() endswith() <-- keren 
cek_start = "Jungkook Oppa".startswith("Jungkook")
print("Start = " + str(cek_start))

cek_end = "Jungkook Oppa".endswith("Oppa")
print("End = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = ' ehm '.join(pisah)
print(gabung)

gabung = "akuehmsayangehmkamu"
print(gabung.split('ehm'))

## alokasi karakter rjust() ljust() center()
kanan = "kanan".rjust(20,"=")
print("'" + kanan + "'")
kiri = "kiri".ljust(20,"=")
print("'" + kiri + "'")
tengah = "tengah".center(20,"=")
print("'" + tengah + "'")

# kebalikannya -> strip ()
tengah = tengah.strip("=") # menghilangkan tanda = 
print("<"+tengah+">")