import pygame as pg
import sys
from random import randint

pg.init()

screen = pg.display.set_mode((400, 600))
bg = pg.image.load('assets/bg.png')
screen.blit(bg,(0,0))

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('assets/Player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 500
        
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('assets/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(0 , 360)
        self.rect.y = -100 
        
    def update(self):
        self.rect.move_ip(0,10)
        if self.rect.y > 700:
            self.rect.y 
        
player = Player()
eenmy = Enemy()
sprites = pg.sprites.Group()
sprites.add(Player) 
sprites.add(Enemy)

       

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.flip()
    sprites.update()
    sprites.draw(screen)
    
    
    clock.tick(60)
