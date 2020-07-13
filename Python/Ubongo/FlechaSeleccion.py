import pygame
flc = pygame.image.load('img/triangulo.png')

class arrow(object):
    
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
            win.blit(flc, (self.x, self.y))