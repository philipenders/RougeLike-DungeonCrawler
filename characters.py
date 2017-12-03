class Character(object):
    def __init__(self):
        self.hp = 10



class Player(Character):
    def __init__(self):
        super(Player,self).__init__()


class Enemy(Character):
    def __init__(self, enemy_type):
        super(Enemy,self).__init__()


class NPC(Character):
    def __init__(self):
        super(NPC,self).__init__()
