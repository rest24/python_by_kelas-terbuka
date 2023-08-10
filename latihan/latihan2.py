'''#No 1
#-------0++++++5------8++++++11------
inputPengguna = float(input("Masukkan Angka :"))

#-------0++++++
#memeriksa angka Lebih Besar dari 0
a = (inputPengguna > 0)
print("Lebih Dari 0 = ", a)
#+++++++5------
#memeriksa angka kurang dari 5
b = (inputPengguna < 5)
print("Kurang Dari 5 = ",b)
#-------8++++++++
#memeriksa angka Lebih Besar dari 8
c = (inputPengguna > 8)
print("Lebih Dari 8 = ", c)
#+++++++11------
#memeriksa angka kurang dari 11
d = (inputPengguna < 11)
print("Kurang Dari 11 = ", d)
hasil = (a and b) or (c and d )
print("Angka yang anda masukkan adalah = ",hasil)
'''


print("\n",20*"=","\n")
#No 2
#++++++0------5++++++8------11+++++++

inputUser = float(input("Masukkan Angka :"))

#+++++++0-------
#memeriksa angka Kurang dari 0
e = (inputUser < 0)
print("Kurang Dari 0 = ",e)
#-------5+++++++
#memeriksa angka Lebih dari 5
f = (inputUser > 5)
print("Lebih Dari 5 = ",f)
#+++++++8-------
#memeriksa angka Kurang dari 8
g = (inputUser < 8)
print("Kurang Dari 8 = ",g)
#-------11+++++++
#memeriksa angka Lebih dari 11
h = (inputUser > 11)
print("Lebih Dari 11 = ",h)
#hasil
hasil = (e or f) and (g or h )
print("Angka yang anda masukkan adalah = ",hasil)
