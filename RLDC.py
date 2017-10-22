class PlayerCharacter:

    def __init__(self):
        self.name = "Player"
        self.health = 3
        self.inventory = [0]
        self.canopendoor = (self.inventory[0]==1)
        self.x_loc = 0
        self.y_loc = 0
        

    def UpdateInventory(self, key):
        print key.x_key_location
        print key.y_key_location
        print self.x_loc
        print self.y_loc
        if key.x_key_location < self.x_loc and key.x_key_location+10 > self.x_loc:
            if key.y_key_location < self.y_loc and key.y_key_location +10 > self.y_loc:
                self.inventory[0] =1
                self.canopendoor = (self.inventory[0]==1)

class Key:

    def __init__(self, x_key_location, y_key_location):
        self.x_key_location = x_key_location
        self.y_key_location = y_key_location


#Checks if collision works
myKey = Key(10,10)
myPlayer = PlayerCharacter()

print myPlayer.canopendoor

myPlayer.x_loc +=15
myPlayer.y_loc +=15

myPlayer.UpdateInventory(myKey)

print myPlayer.canopendoor
