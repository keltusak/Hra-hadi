import random

class Game:
    def _init_(self):
        pass
    def players(self):
        self.players = int(input("Chose number of players in game: "))
        return self.players
        
class Field(Game):
    list = []
    for i in range (0,100):
        list.append(i)

class Player(Game):
    def _init_(self, player, position):
        self.position = position
        self.player = player

    def __init__(self, name):
        self.name = name

    def roll():
        move = random.randint(1,6)
        while (move % 6 == 0):
            move += random.randint(1,6)
        position += move
        return roll
           
                
            
                
       


class Snake(Field):
    pass
class Ladder(Field):
    pass        
