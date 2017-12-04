import characters

class Item(object):
    def __init__(self,name,owner):
        self.value = 3
        self.owner = owner
        self.name = name

class Weapon(Item):
    def __init__(self, damage):
        super(Weapon,self).__init__()
        self.base_damage = self.owner.strength +damage
        self.value = (3*damage) + self.value

class Armor(Item):
    def __init__(self):
        super(Armor, self).__init__()


class Boots(Item):
    def __init__(self):
        super(Boots,self).__init__()

class MiscWearable(Item):
    def __init__(self):
        super(MiscWearable,self).__init__()


class MiscOther(Item):
    def __init__(self):
        super(MiscOther,self).__init()




pointy_stick = Weapon(characters.Player.weapon,2)

myPlayer = Player("Jask")

