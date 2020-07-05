import pygame
clc = pygame.image.load('cronometro.png')

class stopwatch(object):
    
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.num = 0
        self.width = width
        self.height = height
        self.vel = 15
        self.visible = True
    def draw(self, win):
        if self.visible:
            win.blit(clc, (self.x, self.y))