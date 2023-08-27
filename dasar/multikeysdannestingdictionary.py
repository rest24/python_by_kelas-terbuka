import datetime

mahasiswa1 = {
    'nama' : 'ucup surucup',
    'nim' : '192832818',
    'sks_lulus' : 130,
    'beasiswa' : False,
    'lahir' : datetime.datetime(2000,2,18)
}
mahasiswa2 = {
    'nama' : 'otong surotong',
    'nim' : '1928327383',
    'sks_lulus' : 113,
    'beasiswa' : True,
    'lahir' : datetime.datetime(2001,7,5)
}
mahasiswa3 = {
    'nama' : 'asep sikasep',
    'nim' : '1928328223',
    'sks_lulus' : 140,
    'beasiswa' : False,
    'lahir' : datetime.datetime(1998,10,7)
}

data_mahasiswa = {
    'MAH001' : mahasiswa1,
    'MAH002' : mahasiswa2,
    'MAH003' : mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<17}{'SKS':<4}{'Beasiswa':<9}{'Lahir':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    
    print(f"{KEY:<6} {NAMA:<17}{SKS:<4}{BEASISWA:^9}{LAHIR:<10}")
