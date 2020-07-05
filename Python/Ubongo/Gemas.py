import pygame
class gem(object):
    gema = [pygame.image.load('gema1.png'), pygame.image.load('gema2.png'), pygame.image.load('gema3.png'), pygame.image.load('gema4.png'), pygame.image.load('gema5.png'), pygame.image.load('gema6.png')]
    def __init__(self,x,y,width,height, number):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.number = number
        self.visible = True
    def draw(self, win):
        if self.visible == True:
            win.blit(self.gema[self.number], (self.x, self.y))