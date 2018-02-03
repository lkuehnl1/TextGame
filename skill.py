#!/usr/bin/python


# ------------------ Base class Skill --------------------------------
class Skill:
    def __init__(self, pts):
        """
        Baseclass skill initialized with some number of pts        
        """
        self.pts = pts
        
    def desc(self):
        """
        Description of this specific skill (debugging/logging purposes)
        """
        return 'No skill..'

    def add(self, pts):
        """
        Add points to current level in this skill
        """
        self.pts += pts # cap at some maximum ?

    def sub(self, pts):
        """
        Subtract points to current level in this skill
        """
        self.pts = max(0, self.pts-pts) # always >= 0

    def Levels(self):
        """
        Access the points placed in this skill.
        """
        return self.pts

        
# ------------------ Derived Skill classes implementation -----------------------------
class Agility(Skill):
    def desc(self):
        return "Agility: affects movement speed and attack speed."

    
class Intelligence(Skill):
    def desc(self):
        return "Intelligence: affects mana pool and spell casting "

    
class Strength(Skill):
    def desc(self):
        return "Strength: affects damage and HP"

    
class Hacking(Skill):
    def desc(self):
        return "Hacking: affects ability to gain knowledge from AI."

    
class Sight(Skill):
    def desc(self):
        return "Sight: bio-enhanced xray vision!?"

    
class Nanite(Skill):
    def desc(self):
        return "Nanite: control nanintes more completely/wifi signal is stronger"

