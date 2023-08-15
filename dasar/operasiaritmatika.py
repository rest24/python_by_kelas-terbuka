a=15
b=10

# Operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)

# Operasi pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)

# Operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

# Operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

# Operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)

# Operasi modulus %
hasil = a % b
print(a,'%',b,'=',hasil)

# Operasi floor division //
hasil = a // b
print(a,'//',b,'=',hasil)

# Prioritas operasi, operational precedence
''''
    1. ()
    2. exponen **
    3. perkalian dan teman - teman * / % ** //
    4. pertambahan dan pengurangan + -
'''
x=3
y=2
z=4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=', hasil)
# Tanda Kurung akan mengambil langkah pertama
hasil = ( x + y ) * z
print('(',x,'+',y,')','*',z,'=', hasil)