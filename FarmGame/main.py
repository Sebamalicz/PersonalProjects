import pygame as py
import sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        py.display.set_caption('Farming Sim')
        self.clock = py.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()

            dt = self.clock.tick(60) / 1000
            self.level.run(dt)
            py.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()