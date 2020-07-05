import pygame
py3 = pygame.image.load('p3.png')
class playerCPU(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = False
    def draw(self, win):
        if self.visible:
            win.blit(py3, (self.x , self.y))