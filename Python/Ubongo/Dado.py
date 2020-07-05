import pygame
import random

class dice(object):
    dd = [pygame.image.load('dado5.png'), pygame.image.load('dado4.png'), pygame.image.load('dado6.png') 
    , pygame.image.load('dado3.png') , pygame.image.load('dado2.png') , pygame.image.load('dado1.png')]
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.number = 0
        self.hitbox = (self.x,self.y, 65,57)
        self.throwed = False
    def ThrowDice(self):
        self.number = random.choice(range(0,6))
    def draw(self, win):
        pygame.draw.circle(win, (0,0,0), (self.x +32, self.y +29),65)
        win.blit(self.dd[self.number], (self.x , self.y))
        pygame.draw.rect(win, (0,255,0), self.hitbox,2)
    