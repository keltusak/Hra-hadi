import random

class Game:
    def _init_(self):
        pass
    def players(self):
        self.players = int(input("Chose number of players in game: "))
        
        
class Field(Game):
    list = []
    for i in range (0,100):
        list.append(i)

class Player(Game):
    def _init_(self):
        self.position = 1

    def roll(self):
        move = random.randint(1,6)
        while (move % 6 == 0):
            move += random.randint(1,6)
        position += move
        return roll
           
                
            
                
       


class Snake(Field):
    pass
class Ladder(Field):
    pass        
