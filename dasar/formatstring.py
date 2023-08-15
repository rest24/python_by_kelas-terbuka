# format string

# contoh generic
# string
nama = "marline"
format_str = f"hallo {nama}"

print(format_str)

# boolean
boolean = False
format_str = f"boolean = {boolean}"
print (format_str)

# angka 
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 17
format_str = f"Bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 200000000
format_str = f"ribuan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.55416
format_str = f"desimal = {angka:.3f}"
print(format_str)

# menampilkan leading zero
angka = 2005.55457
format_str = f"desimal = {angka:010.2f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -30
angka_plus = 70.46546
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}" 

print(format_plus)
print(format_minus)

# memformat persen 
persentase = 0.057
format_persen = f"persen = {persentase:.2%}"

print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 50
format_string = f"harga total = Rp {harga*jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hexa = {hex(angka)}"

print (format_binary)
print (format_octal)
print (format_hex)
