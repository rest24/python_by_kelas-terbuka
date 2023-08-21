class Hero : # template
    def __init__(self,inputName,inputHealt,inputPower,inputArmor):
        # instance variable
        self.name = inputName
        self.healt = inputHealt
        self.power = inputPower
        self.armor = inputArmor
        
hero1 = Hero ("sukimin",100,10,4)
hero2 = Hero ("saodah",100,3,1)

print (hero1.__dict__)
print (hero2.__dict__)