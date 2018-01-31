class Background:
    def __init__(self, description):
        self.d = description
print ('what class would you like to learn more about? Soldier?')
x= Background('you are a military trained badass')
z=input()
if z == 'Soldier':
    print(x.d)