data0 = [1,2]
data1 = [2,3]
data_list_biasa = [1,2,3,4]

print(f"list biasa = {data_list_biasa}")
list2dimensi = [data0,data1,data_list_biasa]
print(list2dimensi)

# contoh penggunaan
peserta0 = ["ucup",25,"laki-laki"]
peserta1 = ["otong",10,"laki-laki"]
peserta2 = ["dedeh",50,"perempuan"]

list_peserta = [peserta0,peserta1,peserta2]
print(f"peserta =\n {list_peserta}")

for peserta in list_peserta :
    print (f"nama\t\t: {peserta[0]}")
    print (f"umur\t\t: {peserta[1]}")
    print (f"jenis kelamin   : {peserta[2]}\n")
    
# dengan reference
list_copy = list_peserta.copy()
print(f"peserta =\n {list_copy}")
peserta0[0] = "michael"
print(f"peserta =\n {list_peserta}")
print(f"peserta =\n {list_copy}")
