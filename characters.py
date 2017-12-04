import random
class Character(object):
    def __init__(self):
        self.hp = 10
        self.strength = 10 #Base damage
        self.defense = 5
        self.speed = 5 #number of tiles movable per turn
    def attack(self, target):
        target.hp -= max[(self.weapon.base_damage - (target.defense +target.armor.base_armor)), 1]

class Player(Character):
    def __init__(self,name):
        super(Player,self).__init__()
        self.weapon = "pointy_stick"


class Enemy(Character):
    def __init__(self, enemy_type):
        super(Enemy,self).__init__()


class NPC(Character):
    def __init__(self):
        super(NPC,self).__init__()
