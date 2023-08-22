class Hero :
    # class variable
    jumlah = 0
    __privateJumlah = 0
    def __init__(self,name,health) :
        self.name = name
        self.health = health
        
        # variable instance private
        self.__private = "privasi"
        
        # variable instance protected
        self._protected = "proteksi"
        
lina = Hero("lina",100)

print(lina.__dict__)
#print(lina._protected)
#lina.private =  "test"
lina._protected = "test"
print(Hero.__dict__)
#print(lina._protected)
#print(lina.private) # tidak bisa karena di private
#print(Hero.__privateJumlah) # tidak bisa karena di private
