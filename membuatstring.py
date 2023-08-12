data = "ini adalah string"
print(data)
print(type(data))

# cara membuat string
'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''
data = 'Mengunakan singe quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Hallo, apa kabar?"')
print("'Hallo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("C:\\User\\ucup")

#tab
print("ucup\t\t\totong, semakin jauhan")

#backspace
print("ucup \botong, jadi deketan")

# newline
print("baris pertama. \nbaris kedua.") # LF -> Line Feed
print("baris pertama. \rbaris kedua.") # CR -> Carriage Return
print("baris pertama. \r\nbaris kedua") # CRLF -> Line Feed Carriage Return

# 3. String literal atau raw

# hati-hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string 
print(r'C:\new folder')

# multiline literal string
print("""
      Nama : Restu Andryana 
      Kelas : 15.4B.12
      
      """)

# multiline literal string dan RAW
print(r"""
      Nama : Restu Andryana
      Kelas : 15.4B.12\new normal
      Website : www.RestuAnd.com/newID
      """)