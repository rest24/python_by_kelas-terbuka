# latihan

# kalkulator sederhana
print(20*"=")
print("Kalkulator Sederhana")
print(20*"="+"\n")

angka1 = float(input("masukkan angka pertama = "))
operator = input("operator(+,-,x,/) : ")
angka2 = float(input("Masukkan angka kedua = "))

# percabangannya
if operator == '+':
    hasil = angka1 + angka2
    print(f"Hasilnya adalah {hasil}")
elif operator == '-':
    hasil = angka1 - angka2
    print (f"hasilnya adalah {hasil}")
elif operator == 'x' or operator == '*':
    hasil = angka1 * angka2 
    print (f"Hasilnya adalah {hasil}") 
elif operator== '/' or operator == ":":
    hasil = angka1 / angka2
    print (f"Hasilnya adalah {hasil}")
else :
    print("Masukkan yang bener dong ..!!")
print ("Akhir dari program, Terimakasih")