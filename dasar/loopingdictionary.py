# looping dictionary

teman_teman = {
    "cup" : "ucup surupcup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung",
    "sep" : "asep sikasep",
    "cuy" : "ucuy surucuy"
}

# looping first try (yang keluar adalah key nya)
for teman in teman_teman :
    print(teman)
    
# operator untuk mengambil item / iterable
katakunci = teman_teman.keys()
print(katakunci)

for kkunci in teman_teman.keys() :
    print(teman_teman.get(kkunci))
    
nilai = teman_teman.values()
print(nilai)

for nilai in teman_teman.values() :
    print(nilai)
    
daftar = teman_teman.items()
print(daftar)

for daftar in teman_teman.items() :
    print(daftar)
    
for kkunci,nilai in teman_teman.items() :
    print(f"key = {kkunci}, value = {nilai}")