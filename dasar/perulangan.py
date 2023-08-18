# perulangan (loop)

#for kondisi :
#    aksi

# ini dengan list
angka_list = [0,1,2,3,4,5]
print (angka_list)

for i in angka_list:
    print(f" i sekarang {i}")
print("Akhir dari program list\n")

# ini dengan range
angka_range = range(1,25)
for i in angka_range:
    print(f" i sekarang {i}")
#    print("saya keren")
print("Akhir dari program range\n")

# menggunakan string

data_str = "saya ganteng banget"
for huruf in data_str :
    print(huruf)
print("Akhir dari program String\n")