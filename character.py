#!/usr/bin/python

import skill as S
import weapon as W

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
                 age = 24):      # years
        self.name = name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age

    def desc(self):
        gen = ['male', 'female', 'android']
        print('Name: %s' % self.name)
        print('Age: %d' % self.age)
        print('Gender: %s' % gen[self.gender])
        print('Height(m): %d' % self.height)
        print('Weight(kg): %d' % self.weight)


# ------------------ Base class Character --------------------------------

# todo: add Equipment (armor, weapons, ammo), Items(medkit,stimpak,drugs,keys,tech,etc.)
class Character:
    def __init__(self,
                 bio="",
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
        self.Skills = [S.Skill(0)] # for now, initialize skills to 0
        self.Weapons = [W.Weapon()]
        self.bio = bio
        self.Props = props

    def desc(self):
        """
        Description of this character (logging/debugging)
        prints: all contained descriptions of Skills/Inventory/Properties
        """
        print('---Skills---')
        for s in self.Skills:
            print(' %s - %d Levels' % (s.desc(), s.Levels()))
        print('---Properties---')
        print(' %s' % self.Props.desc())
        print('---Bio---')
        print(self.bio)
""" TODO
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
"""


# ------------------ Derived Character implementation -----------------------------
class Scientist(Character):
    def __init__(self, bio="", props=None):
        Character.__init__(self, bio, props)
        self.bio = """ You are a Scientist! """
    pass


class Marine(Character):
    def __init__(self, bio="", props=None):
        Character.__init__(self, bio, props)
        self.bio = """ You are a marine! Get to the choppa!!"""
    pass


class Medic(Character):
    def __init__(self, bio="", props=None):
        Character.__init__(self, bio, props)
        self.bio = """ You are a Medic! """
    pass


class Technician(Character):
    def __init__(self, bio="", props=None):
        Character.__init__(self, bio, props)
        self.bio = """ You are a Technician! """
    pass


class Android(Character):
    def __init__(self, bio="", props=None):
        Character.__init__(self, bio, props)
        self.bio = """ You are a Android! """
    pass
