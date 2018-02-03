#!/usr/bin/python


# ------------------ Base class Skill --------------------------------
class Skill:
    def __init__(self, pts):
        """
        Baseclass skill initialized with some number of pts        
        """
        self.pts = pts
        
    def desc():
        """
        Description of this specific skill (debugging/logging purposes)
        """
        raise NotImplementedError("Subclass must implement abstract method")

    def add(pts):
        """
        Add points to current level in this skill
        """
        self.pts += pts # cap at some maximum ?

    def sub(pts):
        """
        Subtract points to current level in this skill
        """
        self.pts = max(0, self.pts-pts) # always >= 0

    def Levels():
        """
        Access the points placed in this skill.
        """
        return pts

        
# ------------------ Derived Skill classes implementation -----------------------------
class Agility(Skill):
    def desc():
        return "Agility: affects movement speed and attack speed."

    
class Intelligence(Skill):
    def desc():
        return "Intelligence: affects mana pool and spell casting "

    
class Strength(Skill):
    def desc():
        return "Strength: affects damage and HP"

    
class Hacking(Skill):
    def desc():
        return "Hacking: affects ability to gain knowledge from AI."

    
class Sight(Skill):
    def desc():
        return "Sight: bio-enhanced xray vision!?"

    
class Nanite(Skill):
    def desc():
        return "Nanite: control nanintes more completely/wifi signal is stronger"

