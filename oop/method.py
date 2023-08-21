class Hero:
    # class variable 
    jumlah_hero = 0
    def __init__(self,inputName,inputHealt,inputPower,inputArmor):
        # instance variable
        self.nama=inputName
        self.health=inputHealt
        self.power=inputPower
        self.armor=inputArmor
        Hero.jumlah_hero += 1
    # void function, method tanpa return, tanpa argument
    def siapa (self):
        print("namaku adalah " + self.nama)
    # method dengan argument, tanpa return
    def tambahDarah (self,tambah):
        self.health += tambah
    # method dengan return 
    def ambiDarah (self):
        return self.health

hero1 = Hero ('sniper',100,10,5)
hero2 = Hero ('mario bros',90,5,10)

hero2.siapa()
hero1.tambahDarah(10)

print (hero1.ambiDarah())