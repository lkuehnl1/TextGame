class Background:
    def __init__(self, background, description):
        self.b = background
        self.d = description
print('which background would you like to learn more about? Soldier?')
x = Background("Soldier:","You are a millitary trained badass")
z=input()
if z == 'Soldier':
    print(x.b, x.d)