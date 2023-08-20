## teknik menduplikat list

a = ["ucup","otong","dudung"]
print (f"a = {a}")

b = a # pass by reference
print (f"b = {b}")

# kita akan merubah member dari a

# ini akan merubah kedua list
a[1] = "michael"
b.sort()
print (f"a = {a}")
print (f"a = {b}")

# addres dari kedua list a dan b 
print (f"address a = {hex(id(a))}")
print (f"address b = {hex(id(b))}")

# menduplikat list dengan copy
print ("membuat list c dengan a.copy()")
c = a.copy() # full duplikat / data baru

print (f"address a = {hex(id(a))}")
print (f"address b = {hex(id(b))}")
print (f"address c = {hex(id(c))}")

print (f"a = {a}")
print (f"a = {b}")
print (f"c = {c}")

print ("ubah data ke 0")
c[0] = "dadang"
print (f"a = {a}")
print (f"a = {b}")
print (f"c = {c}")

print ("ubah data ke 1")
a[1] = "otong"
print (f"a = {a}")
print (f"a = {b}")
print (f"c = {c}")
