import pygame as py
from settings import *
from support import *

class Player(py.sprite.Sprite):

    def __init__(self, pos, group):
        super().__init__(group)

        self.import_assets()

        # general setup
        self.image = py.Surface((32, 64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)

        # movement attributes
        self.direction = py.math.Vector2()
        self.pos = py.math.Vector2(self.rect.center)
        self.speed = 200

    def import_assets(self):
        self.animations = {'ForwardDown': [], 'ForwardUp': [], 'RightUp': [],
                            'RightDown': [], 'LeftUp': [], 'LeftDown': []}

        for animation in self.animations.keys():
            full_path = "/Sprites/ZombiePlayer" + animation 
            self.animations[animation] = import_folder(full_path)

    def input(self):
        keys = py.key.get_pressed()

        if keys[py.K_UP]:
            self.direction.y = -1
        elif keys[py.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if keys[py.K_LEFT]:
            self.direction.x = -1
        elif keys[py.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, dt):

        # normalizing a vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        #horizontal movement
        self.pos.x += self.direction.x * self.speed * dt 
        self.rect.centerx = self.pos.x

        #vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.move(dt)
