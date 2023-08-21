class Hero : # template
    pass

hero1 = Hero() # onject / instance (instantiate)
hero2 = Hero ()
hero3 = Hero ()

hero1.nama = "kelly"
hero1.darah = 100

hero2.nama = "Alok"
hero2.darah = 200

hero3.nama = "otong"
hero3.darah = 1000

print(hero1)
print(hero1.__dict__)
print(hero1.nama)