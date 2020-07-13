import pygame

py = [pygame.image.load('img/p1.png'), pygame.image.load('img/p2.png')]

class player(object):
    def __init__(self,x,y,width,height, num, pos):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = False
        self.num = num
        self.cpu = False
        self.listgems = [0]*6
        self.pos = pos
        self.vel = 30
        self.maxpos = 0
        self.minpos = 0
    def draw(self, win):
        if self.visible:
            win.blit(py[self.num], (self.x, self.y))
    def move_up(self):
        self.y = self.y - self.vel
        self.pos = self.pos -1
        if self.pos < 0:
            self.pos = 0
            self.y = self.y + self.vel
        if self.pos < self.minpos:
            self.y = self.y + self.vel
            self.pos = self.pos +1
    def move_down(self):
        self.y = self.y + self.vel
        self.pos = self.pos +1
        if self.pos > self.maxpos:
            self.y = self.y - self.vel
            self.pos = self.pos -1
        if self.pos > 5:
            self.pos = 5
            self.y = self.y - self.vel
        
