class Item(object):
    def __init__(self):
        self.value = 12


class Weapon(Item):
    def __init__(self):
        super(Weapon,self).__init__()



myWeapon = Weapon()

