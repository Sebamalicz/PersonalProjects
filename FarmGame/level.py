import pygame as py
from settings import *
from player import Player 

class Level:
    def __init__(self):
        # get the display surface
        self.displaySurface = py.display.get_surface()

        # sprite groups
        self.allSprites = py.sprite.Group()

        self.setup()

    def setup(self):
        self.player = Player((640, 360), self.allSprites)

    def run(self, dt):
        self.displaySurface.fill('black')
        self.allSprites.draw(self.displaySurface)
        self.allSprites.update(dt)