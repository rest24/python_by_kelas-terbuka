# Belajar Casting 
# Merubah dari satu tipe ke tipe lain
# tipe data = int, floar, string, bool

## INTEGER 
data_int = 9;
print ("====Data Integer====")
print("data = ", data_int ,", type  =", type(data_int))

data_float=float(data_int)
data_string=str(data_int)
data_bool=bool(data_int) # Akan false jika nilai integer = 0
print("data = ", data_float ,", type  =", type(data_float))
print("data = ", data_string ,", type  =", type(data_string))
print("data = ", data_bool ,", type  =", type(data_bool))

## FLOAT
data_float = 2.2;
print ("====Data Float====")
print("data = ", data_float ,", type  =", type(data_float))

data_int=int(data_float) # Akan dibulatkan kebawah
data_string=str(data_float)
data_bool=bool(data_float) # Akan false jika nilai integer = 0
print("data = ", data_int ,", type  =", type(data_int))
print("data = ", data_string ,", type  =", type(data_string))
print("data = ", data_bool ,", type  =", type(data_bool))

## BOOLEAN
data_bool = True;
print ("====Data Bool====")
print("data = ", data_bool ,", type  =", type(data_bool))

data_int=int(data_bool) # Akan dibulatkan kebawah
data_string=str(data_bool)
data_float=float(data_bool) # Akan false jika nilai integer = 0
print("data = ", data_int ,", type  =", type(data_int))
print("data = ", data_string ,", type  =", type(data_string))
print("data = ", data_float ,", type  =", type(data_float))


## STRING
data_string = "95";
print ("====Data String====")
print("data = ", data_string ,", type  =", type(data_string))

data_int=int(data_string) # String harus angka
data_float=float(data_string) # String harus angka
data_bool=bool(data_string) # False jika String kosong
print("data = ", data_int ,", type  =", type(data_int))
print("data = ", data_float ,", type  =", type(data_float))
print("data = ", data_bool ,", type  =", type(data_bool))
