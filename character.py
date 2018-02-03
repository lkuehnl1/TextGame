#!/usr/bin/python

import sys

class CharacterProps:
    """
    Simple data structure with constant properties for this character
    Like: name, gender, age, height, and background story
    """
    def __init__(self,
                 name = "",
                 gender = 0,     # encoding 0 = 'male', 1 = 'female', 2 = 'android'/'other'
                 height = 1.2,   # meters
                 weight = 82,    # kg (important for low/high gravity environments)
                 age = 24,       # years
                 other=""):
        self.name = name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age
        self.background = ""
        self.other = other

    def set_background(self, b):
        """
        Set/update a background story for the character
        """
        self.background = b

    def get_background(self):
        return self.background

    def set_other(self, o):
        """
        Sets 'other' information about this character, if any
        """
        self.other = o

    def desc(self):
        gen = ['male', 'female', 'android']
        print('Name: %s' % self.name)
        print('Age: %d' % self.age)
        print('Gender: %s' % gen[self.gender])
        print('Height(m): %d' % self.height)
        print('Weight(kg): %d' % self.weight)
        print('--Background--')
        print(background)

        
# ------------------ Base class Character --------------------------------
class Character:    
    def __init__(self,
                 skills=[],
                 armor=[],
                 weapons=[],
                 ammo=[],
                 keys=[],
                 tech=[],
                 props=None):
        """
        Base class character:
        skills: array of initial levels (skills-pts) for this character
        armor:  clothes/hats/shirts/pants/shoes each has an armor characteristic
        ammo:   ammo will have a 'type' which must be associated with the proper gun type
        keys:   in case we want to 'unlock' areas/doors/regions of the map
        tech:   things like nanite control/lasers/AI-related/hacking-related
        props:  CharacterProps class
        """
        self.Skills = skills
        self.Armor = armor
        self.Weapons = weapons
        self.Ammo = ammo
        self.Keys = keys
        self.Tech = tech
        self.Props = props

    def desc():
        """
        Description of this character (logging/debugging)
        prints: all contained descriptions of Skills/Inventory/Properties
        """
        print('---Skills---')
        for s in Skills:
            print(' %s - %d Levels' % s.desc(), s.Levels())
        print('---Armor---')
        for a in Armor:
            print(' %s' % a.desc())
            print(' %s' % a.print_status())
        print('---Weapons---')
        for w in Weapons:
            print(' %s' % w.desc())            
            print(' %s' % w.print_status(Ammo))
        print('---Keys---')
        for k in Keys:
            print(' %s' % k.desc())
        print('---Tech---')
        for t in Tech:
            print(' %s' % t.desc())
        print('---Properties---')
        for p in Props:
            print(' %s' % p.desc())            

            
            
# ------------------ Derived Character implementation -----------------------------
class Scientist(Character):
    pass

class Marine(Character):
    pass

class Medic(Character):
    pass

class Technician(Character):
    pass

class Android(Character):
    pass
