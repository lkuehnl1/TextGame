from time import sleep
import random
class Monster:                                  #class representing enemies
    def __init__(self, name, hp, atkpwr):
        self.name = name
        self.hp = hp
        self.atkpwr = atkpwr
class Player:
    def __init__(self, name, hp, atkpwr):
        self.name = name
        self.hp = hp
        self.atkpwr = atkpwr
a = Monster('Android',50, 10)
m = Monster('Mechanized Tank', 75, 15)
p = Player('You', 100, 15)

monsterpool = [m, a]
x=random.choice(monsterpool)
print("A hulking", x.name, "stands before you.") ; sleep(1)
while x.hp > 0:
    print(x.name,"has", x.hp,"HP. \nWill you fight, use, or flee?",)
    action = input()
    if action == "fight":
        print(p.name, "dealt", p.atkpwr, "points of damage") ; sleep(1)
        x.hp = x.hp-p.atkpwr
        print(x.name, "felt the pain!") ; sleep(1)
    if action == "use":
        print('you restored 10 points of health')
    if action == "flee":
        y=random.random()
        if y<.5:
            print("You lived to fight another day! \nSee you next time. :)")
            exit()
        print(p.name, "did not get away")

    print(x.name, "blasts you with a particle cannon! OUCH") ; sleep(1)
    p.hp = p.hp-x.atkpwr
    print("You now have", p.hp,"HP") ; sleep(1)
