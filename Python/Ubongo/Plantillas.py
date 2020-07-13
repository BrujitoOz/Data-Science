import pygame

CodPlantilla = [
    [(8, 6, 4), (11, 0, 7), (0, 8, 6), (3, 0, 10), (0, 10, 6), (6, 7, 3)],
    [(5, 10, 4), (4, 6, 8), (0, 10, 6), (4, 9, 6), (6, 4, 10), (6, 7, 3)],
    [(0, 6, 10), (9, 7, 0), (8, 4, 5), (4, 10, 6), (3, 11, 0), (1, 9, 10)],
    [(8, 0, 10), (6, 9, 5), (2, 6, 10), (7, 10, 2), (8, 5, 6), (6, 8, 7)],
    [(1, 6, 10), (4, 7, 5), (11, 0, 4), (1, 11, 6), (2, 1, 8), (0, 8, 4)],
    [(6, 5, 7), (0, 7, 10), (8, 10, 1), (6, 4, 10), (0, 9, 7), (8, 0, 6)],
    [(9, 5, 3), (6, 10, 2), (0, 11, 10), (7, 8, 6), (10, 6, 5), (9, 10, 4)],
    [(6, 9, 7), (8, 6, 5), (3, 8, 6), (7, 10, 3), (11, 6, 7), (3, 10, 6)],
    [(5, 6, 10), (7, 9, 6), (6, 7, 10), (2, 10, 5), (7, 5, 8), (9, 0, 10)],
    [(4, 7, 10), (6, 4, 10), (0, 10, 6), (8, 1, 10), (3, 7, 6), (6, 8, 0)]
]

CodPlantillaColission = [
    [True, True, True, False, True, True, True, True, True, True, True, True, True, False, False, False],
    [False, True, True, True, False, True, True, True, True, True, True, True, False, False, True, True],
    [True, True, False, False, True, True, True, False, True, True, True, False, True, True, True, True],
    [True, True, False ,False, True , True ,True, True, True, True, True, False, True, True, True, True],
    [False, True, True, False, False, True, True, False, False, True, True, True, True, True, True, True],
    [True, True, True, False, True, True, True, True, True, True, True, True, False, True, False, False],
    [True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False],
    [True, True, True, True, True, True, True, True, False, True, True, True, False, True, True, False], 
    [False, True, True, True, True, True, True, False, True, True, True, False, True, True, True, True ],
    [False, True, True, False, True, True, True, True, False, True, True, True, False, True, True, True]
]

class template(object):
    pnt = [pygame.image.load('img/plantilla1.png'), pygame.image.load('img/plantilla2.png'), pygame.image.load('img/plantilla3.png'), pygame.image.load('img/plantilla4.png'), pygame.image.load('img/plantilla5.png'), pygame.image.load('img/plantilla6.png'), pygame.image.load('img/plantilla7.png'), pygame.image.load('img/plantilla9.png'), pygame.image.load('img/plantilla10.png'), pygame.image.load('img/plantilla11.png') ]
    def __init__(self,x,y,width,height, number):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.number = 7
        self.CodPieces = CodPlantilla[self.number]
        self.CodColission = CodPlantillaColission[self.number].copy()
        self.completed = False
        self.solv_aux = self.CodColission.copy()
        self.solv_aux2 = self.CodColission.copy()
    def draw(self, win):
        win.blit(self.pnt[self.number], (self.x, self.y),)
    def Is_solved(self):
        cont_solv = 0
        for i in self.solv_aux:
            if i == False:
                cont_solv += 1
        if cont_solv >= 16:
            self.solv_aux = self.CodColission.copy()
            return True    
        self.solv_aux = self.CodColission.copy()
        return False
    
    def Actualizar(self):
        self.CodPieces = CodPlantilla[self.number]
        self.CodColission = CodPlantillaColission[self.number].copy()
        self.solv_aux = self.CodColission.copy()
        self.solv_aux2 = self.CodColission.copy()