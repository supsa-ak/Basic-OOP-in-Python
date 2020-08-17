class Fighter:
    def __init__(s,n):
        s.name = n
        s.health = 100 #predefined parameters
        s.damage = 10  #predefined parameters

    def attack(p,attacker):

        attacker.health = attacker.health - p.damage

    #def showed(p):
     #   print(p.attacker)

sak = Fighter("Sarthak")
pak= Fighter("Prabhu")

pak.attack(sak)

#print(type(Fighter))

#pak.showed()

print(sak.health)

#Fighter.attack(sak)
