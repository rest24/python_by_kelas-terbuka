#membuat gabungan area rentang dari angka

#++++++++3----------10++++++++++

inputUser = float(input("Masukkan angka yang bernilai \n kurang dari 3 \n atau \n lebih besar dari 10 "))

# +++++++3--------
#memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3 )
print(isKurangDari)

#-----------10++++++++++
#memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print(isLebihDari)

#++++++++3----------10++++++++++
isCorret = isKurangDari or isLebihDari
print("Angka yang anda masukkan :",isCorret)

#-----3+++++++++++10-----------
#kasus irisan 
print("\n",15*"=","\n")
inputUser = float(input("Masukkan angka yang bernilai \n lebih besar dari 3 \n dan \n kurang dari 10 "))

#-------3+++++++
#lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 =",isLebihDari)

#++++++10--------
#kurang dari 10
isKurangDari = inputUser < 10
print("kurang dari 10 =",isKurangDari)


#-----3+++++++++++10-----------
isCorret = isKurangDari and isLebihDari
print("Angka yang anda masukkan :",isCorret)
