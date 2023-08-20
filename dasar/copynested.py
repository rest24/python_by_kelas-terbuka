data0 = [1,2]
data1 = [3,4]

data2d= [data0,data1,10]
data2dcopy =data2d.copy() 

print(f"data = {data2d}")
print(f"data copy = {data2dcopy}")

# mengambil data dari nested list
data = data2d[1] [0]
print(f"data = {data}")

# address semuanya
print(f"address asli = {hex(id(data2d))}")
print(f"address copy = {hex(id(data2dcopy))}")

print("address dari member ke 1")
print(f"address asli = {hex(id(data2d[0]))}")
print(f"address copy = {hex(id(data2dcopy[0]))}")

print(f"data copy = {data2dcopy}")
data2d[1] [0] = 5
data2d[2] = 9

print(f"data = {data2d}")
print(f"data copy = {data2dcopy}")

# kita gunakan deepcopy
from copy import deepcopy

data2d= [data0,data1,10]
data_2d_deepcopy = deepcopy(data2d)

print(f"address asli = {hex(id(data2d))}")
print(f"address deep = {hex(id(data_2d_deepcopy))}")

print("address dari member ke 1")
print(f"address asli = {hex(id(data2d[0]))}")
print(f"address deep = {hex(id(data_2d_deepcopy[0]))}")

data2d[1] [0] = 30

print(f"data = {data2d}")
print(f"data copy = {data2dcopy}")
print(f"data deep = {data_2d_deepcopy}")
