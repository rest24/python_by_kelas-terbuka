## operasi

# index   0(-3)  (-2)   2(-1)
data = ["ucup","otong","dudung"]

# mengambil data dari list
data1=data[0]
print(f"data pertama {data1}")
data_akhir = data[-1]
print(f"data terakhir {data_akhir}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data {panjang_data}")

## manipulasi data list

# menambahkan item pada list posisi
print(f"data sebelum ditambah {data}")
data.insert(1,"asep")
print (f"data sesudah ditambah {data}")

# menambah list di akhir
data.append("jajang")
print(f"tambah data diakhir {data}")

# menambah list dengan list
databaru = ["ujang","usep","dadang"]
data.extend(databaru)
print(f"data gabungan \n{data}")

## merubah data

# ubah data ke 2 menjadi michael
data[2]= "michael"
print(f"ubah data otong menjadi {data[2]} list data sekarang \n {data}")

# me remove data
data.remove("ujang")
print(f"remove data {data[5]}, list data sekarang \n {data}")
#data.remove("UJang") # akan error karena huruf tidak sesuai

# me remove data paling belakang
data_akhir = data.pop()
print(f"data akhir sekaranag menjadi \n {data}")
print(data_akhir)