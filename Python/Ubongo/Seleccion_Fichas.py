import pygame

class templaterect(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.yini = self.y
        self.visible1 = True
        self.visible2 = False
        self.visible3 = False
 
    def draw(self, win):
        if self.visible1:
            pygame.draw.rect(win, (0,255,0), (self.x, self.y, self.width, self.height) ,2)
        if self.visible2:
            pygame.draw.rect(win, (0,255,0), (self.x + self.width, self.y, self.width , self.height) ,2)
        if self.visible3:
            pygame.draw.rect(win, (0,255,0), (self.x +self.width+self.width, self.y, self.width, self.height) ,2)