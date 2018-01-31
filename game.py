class Background:
    def __init__(self, background, description):
        self.b = background
        self.d = description
print('which background would you like to learn more about? Soldier? Scholar? Engineer?')
x = Background("Soldier:","You are a millitary trained badass!")
y= Background('Engineer:', 'You have spent years studying. Your mind is strong, but your body is weak.')

z=input()
if z == 'Soldier':
    print(x.b, x.d)
if z == 'Scholar':
    print(y.b, y.d)