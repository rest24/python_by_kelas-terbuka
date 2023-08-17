# Date and time (latihan)

import datetime as dt

print ("Masukkan tanggal,\nbulan dan tahun lahir anda \n")
tanggal = int(input ("Tanggal \t: "))
bulan = int(input ("Bulan \t\t: "))
tahun = int(input ("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah : {tanggal_lahir}")

hari_ini = dt.date.today()
print("hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
print(umur_hari)
print(f"hari nya adalah : {tanggal_lahir:%A}")
print(f"umur anda adalah : {umur_tahun} tahun") 