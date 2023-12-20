import random

class Game:
    def _init_(self):
        pass
    def players(self):
        self.X_players = int(input("Chose number of players in game: "))
        return self.X_players
        
class Field(Game):
    list = []
    for i in range (0,100):
        list.append(i)

    special_field={2:38, 7:14, 8:31, 15:26, 16:6, 28:84, 21:42, 36:44, 46:25, 51:67, 62:19, 64:60, 71:91, 74:53, 78:98, 89:68, 92:88, 95:75, 99:80} 

class Player(Game):
    def _init_(self, player, position):
        self.position = position
        self.player = player

    def __init__(self, name):
        self.name = name

    def roll(self.position):
        move = random.randint(1,6)
        while (move % 6 == 0):
            move += random.randint(1,6)
        self.position += move
        return move
           
                
            
                
       


class Snake(Field):
    pass
class Ladder(Field):
    pass        
