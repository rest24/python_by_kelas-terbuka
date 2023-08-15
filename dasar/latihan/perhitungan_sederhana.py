# Konversi satuan temperatur

# program konversi celcius ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukkan suhu dalam celcius : "))
print("Suhu adalah ",celcius,"Celcius")

#reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ",reamur,"Reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah ",fahrenheit,"Fahrenheit")

#kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin adalah ",kelvin,"Kelvin")



## Farenheit to kelvin
print("\nFARENHEIT to KELVIN\n")

farenheit = float(input('Masukan suhu data Farenheit : '))
print("suhu adalah",farenheit, "Farenheit")

celcius = (5/9) * (farenheit - 32)
kelvin = celcius + 273 
print("suhu dalam Kelvin adalah",kelvin, "Kelvin")


# Kelvin to farenheit
print("\nKELVIN to FARENHEIT\n")

kelvin = float(input('Masukan suhu data Kelvin : '))
print("suhu adalah",kelvin, "Kelvin")

celcius = kelvin - 273
farenheit = ((9/5) * celcius) + 32 
print("suhu dalam Farenheit adalah",farenheit, "Farenheit")