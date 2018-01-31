class Background:
    def Soldier(self):
        return 'you are a tough military trained bad-ass!'
print ('what class would you like to learn more about?')
z=input()
if z == 'Soldier':
    print (Background(Soldier))