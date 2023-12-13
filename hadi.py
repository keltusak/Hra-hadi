import random
import glob

class Game:
    def _init_(self):

    def players():
        players = int(input("Chose number of players in game: "))
        return players
        
class Field(Game):
    list = []
    for i in range (0,100):
        list.append(i)

class Player(Game):
    def _init_(self):
        self.position = 1

    def roll():
        move = random.randint(1,6)
        while (move % 6 == 0):
            move += random.randint(1,6)
        position += move
        return roll
           
                
            
                
       


class Snake(Field):

class Ladder(Field):
        
