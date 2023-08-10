# not, or, and , xor

# NOT
print("====NOT====")
a = True
c = not a
print("Data a =",a)
print("-----NOT-------")
print("Data c =",c)

# OR (jika salah satu true maka hasilnya true)
print("====OR====")
a = False
b = False
c = a or b
print(a ,'or', b ,'=',c)
a = False
b = True
c = a or b
print(a ,'or', b ,'=',c)
a = True
b = False
c = a or b
print(a ,'or', b ,'=',c)
a = True
b = True
c = a or b
print(a ,'or', b ,'=',c)

# AND (jika dua buah true maka hasilnya true)
print("====AND====")
a = False
b = False
c = a and b
print(a ,'AND', b ,'=',c)
a = False
b = True
c = a and b
print(a ,'AND', b ,'=',c)
a = True
b = False
c = a and b
print(a ,'AND', b ,'=',c)
a = True
b = True
c = a and b
print(a ,'AND', b ,'=',c)

# XOR (akan true jika salah satu true,sisanya false)
print("====XOR====")
a = False
b = False
c = a ^ b
print(a ,'XOR', b ,'=',c)
a = False
b = True
c = a ^ b
print(a ,'XOR', b ,'=',c)
a = True
b = False
c = a ^ b
print(a ,'XOR', b ,'=',c)
a = True
b = True
c = a ^ b
print(a ,'XOR', b ,'=',c)