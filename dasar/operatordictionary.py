# operator dictionary
data_dict = {
    "tong" : "otong surotong",
    "cup" : "ucup surucup",
    "dang" : "dadang suradang"
}
# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary : {LENDICT}")

# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print (f"apakah {KEY} ada di data dict : {CHECKKEY} ")

# mengakses value (read) dengan get
#print (data_dict["cup"])
#print (data_dict.get(input("masukan data : "),"kata kunci tidak ditemukan..! ")) # cek key dengan message kata kunci tidak ditemukan

# mengupdate data
#data_dict["cup"] = "ucup si ganteng"
#print (data_dict)
#data_dict[input("kata kuncinya : ")] = input("tambahkan isi data : ")
#print (data_dict)

data_dict.update({"ucup":"ucup si ganteng"})
print (data_dict)
data_dict.update({input("kata kuncinya : ") : input("tambahkan isi data : ")}) # kalau ngga ada datanya di update
print (data_dict)

# mendelete data pada dictionary
del data_dict[input("masukkan kata kunci yang ingin dhapus : ")]
print (data_dict)
