# looping dari list

# for loop
print("For Loop")
kumpulan_angka = [2,4,5,6,34,2,]
for angka in kumpulan_angka :
    print(f"angka = {angka}")
    
peserta = ["ucup","otong","dadang","dudung","odah"]
for nama in peserta :
    print(f"Nama peserta : {nama}")
    
# for loop dan range
print("\nFor Loop dan Range") 
kumpulan_angka = [2,3,4,5,6,7]
panjang = len (kumpulan_angka)
for i in range (panjang):
    print(f"angka = {kumpulan_angka[i]}")
    
# while loop
print("\n While loop")
kumpulan_angka = [2,3,4,5,6,7]
panjang = len (kumpulan_angka)

i = 0
while i < panjang :
    print(f"angka = {kumpulan_angka[i]}")
    i += 1
    
# list comprehension
print("\n List Comprehension")
data = ["ucup",1,2,3,"otong"]
[print(f"\ndata = {i}") for i in data]

angka = [2,3,4,5,6,7]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print("\n Enumerate")
data = ["ucup",1,2,3,"otong"]
for index,data in enumerate(data):
    print(f"data = {data}, index ke - {index}")