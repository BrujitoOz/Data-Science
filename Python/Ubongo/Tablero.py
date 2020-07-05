import pygame

brd1 = pygame.image.load('tablero1.png')
brd2 = pygame.image.load('tablero2.png')

class board(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self, win):
        win.blit(brd1, (self.x , self.y))
        win.blit(brd2, (self.x + 475, self.y))