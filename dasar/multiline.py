# width and multiline

# data
data_nama = "ucup surucup"
data_umur = 20
data_tinggi = 170.2
data_nomor_sepatu = 45

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, timggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# string mutiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama},\numur = {data_umur},\ntimggi = {data_tinggi},\nsepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# String multiline (kutip triplets)
data_string = f"""nama   = {data_nama}
umur   = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# mengatur lebar
data_nama = "ucup"
data_string = f"""nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)
