data_angka = [1,2,3,3,4,5,2,34,1,23,324,5,3,43]
print(f"data = {data_angka}")

# count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f"jumlah angka 4 ada {jumlah_data_4} data")
print(f"jumlah angka 3 ada {jumlah_data_3} data")

# ambil posisi data (index)
data = ["ucup","dadang","ujang","otong"]
index_otong = data.index("otong")
print(index_otong)

# mengurutkan list
print(f"data sbelum diurutkan \n {data_angka}")
data_angka.sort()
print (f"sesudah diurutkan \n {data_angka}")
data.sort()
print (f"sesudah diurutkan \n {data}")

# dibalik /revers
data.reverse()
data_angka.reverse()
print (f"sesudah diurutkan angka \n {data_angka} dan data string \n {data} ")
