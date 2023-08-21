class Hero : # template
    # class varible
    jumlah = 0
    
    def __init__(self,inputName,inputHealt,inputPower,inputArmor):
        # instance variable
        self.name = inputName
        self.healt = inputHealt
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print ("Membuat Hero dengan nama " + inputName)
        
hero1 = Hero ("sukimin",100,10,4)
print(Hero.jumlah)
hero2 = Hero ("saodah",100,3,1)
print(Hero.jumlah)
