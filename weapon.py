#!/usr/bin/python


# ------------------ Base class Weapon --------------------------------
class Weapon:
    def __init__(self, ammo = []):
        """
        Baseclass Weapon
        Ammo: could have multiple types of ammo for one weapon
        """
        self.ammo = ammo
        
    def desc(self):
        """
        Description of this specific skill (debugging/logging purposes)
        """
        raise NotImplementedError("Subclass must implement abstract method")

    def add(self, ammo):
        """
        Add weapon ammo
        """
        raise NotImplementedError("Subclass must implement abstract method")


    def sub(self, ammo):
        """
        Subtract ammo
        """
        raise NotImplementedError("Subclass must implement abstract method")

    def Levels(self):
        """
        Access the level of this weapon (?)
        """
        raise NotImplementedError("Subclass must implement abstract method")



class Pistol(Weapon):
    pass

class Rifle(Weapon):
    pass

class Knife(Weapon):
    pass

class Grenade(Weapon):
    pass

class Laser(Weapon):
    pass
