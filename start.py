#!/usr/bin/env python3
# Soubor:  kameny.py
# Datum:   06.11.2018 10:01
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
############################################################################
import pyglet
import random
import glob


# from pyglet.window.key import LEFT, RIGHT, UP, DOWN, LCTRL
# from pyglet.window.mouse import LEFT as MouseLEFT

import pyglet.window.key
import pyglet.window.mouse

window = pyglet.window.Window(width=800, height=600)
batch = pyglet.graphics.Batch()  # pro optimalizované vyreslování objektů


class SpaceObject(pyglet.sprite.Sprite):
    speed_x=0
    speed_y=0

    def __init__(self, img_path: str, batch=None,position_x=0,position_y=0):

        self.img = pyglet.image.load(img_path)
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2
        self.sprite = pyglet.sprite.Sprite(self.img, batch=batch)
        self.sprite.x = position_x
        self.sprite.y = position_y

    def move(self,dt:float):
        self.sprite.x += self.speed_x * dt * 10
        self.sprite.y += self.speed_y * dt * 5

class Meteor(SpaceObject):

    speed_x=500
    speed_y=500

    def __init__(self, position_x, position_y, batch, img_path = "img/meteorBrown_big1.png"):
        super().__init__(img_path, position_x=position_x, position_y=position_y, batch=batch)
        self.sprite.x = position_x
        self.sprite.y = position_y


class BrownMeteor(Meteor):
    
    def __init__(self, position_x, position_y, batch):
        super().__init__(img_path="img/meteorBrown_big1.png",position_x=position_x, position_y=position_y, batch=batch)
        self.sprite.x = position_x
        self.sprite.y = position_y

class GreyMeteor(Meteor):
     def __init__(self, position_x, position_y, batch):
        self.speed_x=200
        self.speed_y=200
        super().__init__(img_path="img/meteorGrey_big1.png",position_x=position_x, position_y=position_y, batch=batch)
        self.sprite.x = position_x
        self.sprite.y = position_y

meteor1=Meteor(position_x=50, position_y=50,batch=(batch))
meteor2=Meteor(position_x=100, position_y=100,batch=(batch))
meteor3=Meteor(position_x=150, position_y=150,batch=(batch))
meteor4=GreyMeteor(position_x=200, position_y=200,batch=(batch))
   


@window.event
def on_draw():
    window.clear()
    batch.draw()


@window.event
def on_key_press(sym, mod):
    print(sym, mod)


@window.event
def on_key_release(sym, mod):
    print(sym, mod)


@window.event
def on_mouse_press(x, y, button, mod):
    print(x, y, button)
    ship.x = x
    ship.y = y


#def tick(dt):
    #suter.move(dt)
    #bubble.move(dt)
    #bubble2.move(dt)
    #for o in objekty:
        #o.move(dt)
    #print(dt)

#suter = SpaceObject("img/meteorBrown_big1.png", 10, 4)
#bubble = SpaceObject("img/bubble.png", 4, 8)
#bubble2 = SpaceObject("img/bubble.png", 2, 8)
#objekty= []
#for _ in range(22):
    #o = SpaceObject(
        #random.choice(glob.glob("img/*.png")),
        #random.randint(0,20),
        #random.randint(0,20))
    #objekty.append(o)

# funkce tick se spustí 30x za sekundu
#pyglet.clock.schedule_interval(tick, 1 / 30)

# nekonečná smyčka ve které se čeká na události, které se následně obsluhují
pyglet.app.run()
