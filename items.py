#!/usr/bin/python
class item:
    """
    This is meant to be the items themselves (medkit etc,) which are stored in
    class items:
    """
    def __init__(self,
                name = "medkit",):
        self.name = name



class items:
    def __init__(self,
                contents = item()):
        self.contents = contents


    def desc(self):
        print ("Your items are %s" % self.contents)

a = items(item("medkit"))
print(a.desc())
