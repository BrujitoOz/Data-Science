import pygame
import random
pygame.init()
from Plantillas import template, CodPlantilla, CodPlantillaColission
from Fichas import pieces, pzs
from Tablero import board, brd1, brd2
from Dado import dice
from Gemas import gem
from FlechaSeleccion import arrow, flc
from Jugador1 import player, py2
from Jugador2 import playerCPU, py3
from Seleccion_Fichas import templaterect
from Deteccion_col_plantilla import templatecirclescolission



class Game(object):
    def __init__(self):
        self.win = pygame.display.set_mode((1200, 800))
        self.bg = pygame.image.load('mesa.jpg')
        self.run = True
        self.ChoosePos = True
        self.press = False
        self.PieceSelect = 0
        self.completed = False
        self.asd = 0
        self.pls = 0
        self.font = pygame.font.SysFont(' comicsans', 31, True)
        self.Start_Game()
        self.Armar()
        

    def Start_Game(self):
        pygame.display.set_caption("Ubongo")
        jugador = player(200, 0, 0, 0)
        y = random.choice(range(0, 6))
        jugadorcpu = playerCPU(265, 200 - (17 * y), 0, 0)
        tablero = board(165, 25, 914, 200)
        flecha = arrow(150, 200, 0, 0)
        dado = dice(1010, 600, 200, 200)
        plantilla = template(250, 310, 0, 0)
        cuadrado = templaterect(plantilla.x + 130, plantilla.y+45, 42, 57)
        cualalitos = []
        for i in range(4):  
            cualalitos.append(templatecirclescolission(plantilla.x + 367 +( 69*i), plantilla.y+128, 20, 20))
        for i in range(4):  
            cualalitos.append(templatecirclescolission(plantilla.x + 367 +( 69*i), plantilla.y+128 + 69, 20, 20))
        for i in range(4):  
            cualalitos.append(templatecirclescolission(plantilla.x + 367 +( 69*i), plantilla.y+128 + 69 + 69, 20, 20))
        for i in range(4):  
            cualalitos.append(templatecirclescolission(plantilla.x + 367 +( 69*i), plantilla.y+128 + 69 + 69 + 69, 20, 20))
        piezas = []
        gemas = []
        x = 0 
        y = 0
        for j in range(6):
            for i in range(12):
                num = random.choice(range(0,6))
                gemas.append(gem(338 + x, 65 + y, 29 , 27, num))
                x = x +55
            y = y +32
            x = 0
    #dibujar la pantalla 
    def redrawGameWindow(self):
        self.win.blit(self.bg, (0,0))
        tablero.draw(win)
        flecha.draw(win)
        jugador.draw(win)
        jugadorcpu.draw(win)
        for gm in gemas:
            gm.draw(win)
        plantilla.draw(win)
        for pz in piezas:
            pz.draw(win)
            pz.draw_rect_col(win)
            pz.draw_rect2_col(win)
        cuadrado.draw(win)
        for cl in cualalitos:
            cl.draw(win)
        #pieza.draw(win)
        dado.draw(win)
        if completed:
            text = font.render( 'COMPLETED: ', 1, (0, 255, 0))
            win.blit(text, (390, 300))
        text2 = font.render(str(plantilla.CodColission), 1, (0, 0, 0))
        win.blit(text2, (10, 10))
        if dado.throwed:
            text3 = font.render(str(piezas[PieceSelect].x) , 1, (0,0,0))
            win.blit(text3, (10, 300))
            text4 = font.render(str(piezas[PieceSelect].y) , 1, (0,0,0))
            win.blit(text4, (10, 320))
        pygame.display.update()

    def prueba():
          for c in range(piezas[0].cantrect):
             for np in range(3):
                if np != 0:
                   for nc in range(piezas[np].cantrect):
                        if  piezas[0].rect[c][0] >= piezas[np].rect2[nc][0] and piezas[np].rect2[nc][0] + piezas[np].rect2[nc][2] >= piezas[0].rect[c][0]+ piezas[0].rect[c][2]:
                            if  piezas[0].rect[c][1] >= piezas[np].rect2[nc][1] and piezas[np].rect2[nc][1] + piezas[np].rect2[nc][3] >= piezas[0].rect[c][1] + piezas[0].rect[c][3]:
                                return True
                    
    def colision():
        for i in range(16):
            for j in range(3):
                for c in range(piezas[j].cantrect):
                    if  piezas[j].rect[c][0] < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[j].rect[c][0]+ piezas[j].rect[c][2]:
                        if  piezas[j].rect[c][1] < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[j].rect[c][1] + piezas[j].rect[c][3]:
                            plantilla.solv_aux[i] = False
        return
    #ver si las posiciones de las fichas son validas pra FuerzaBruta
    def valid_pos(x, y, p):
        if (x > 900 or y > 700):
            return True
        elif (p == 0):
            for i in [2, 3, 7, 11]:
                if piezas[p].number <= 3:
                    if  piezas[p].x < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[p].x + piezas[p].width:
                        if  piezas[p].y < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[p].y + piezas[p].height:
                                return True
                elif piezas[0].number < 11:
                    if  piezas[p].rect1[0] < cualalitos[i-1].x and cualalitos[i-1].x + cualalitos[i-1].width < piezas[p].rect1[0]+ piezas[p].rect1[2]:
                        if  piezas[p].rect1[1] < cualalitos[i-1].y and cualalitos[i-1].y + cualalitos[i-1].height < piezas[p].rect1[1] + piezas[p].rect1[3]:
                                redrawGameWindow()
                                return True
                    #nose porque i-1 sfklndsfhdsjklashdkjgeshejk
                if  piezas[p].rect2[0] < cualalitos[i-1].x and cualalitos[i-1].x + cualalitos[i-1].width < piezas[p].rect2[0]+ piezas[p].rect2[2]:
                    if  piezas[p].rect2[1] < cualalitos[i-1].y and cualalitos[i-1].y + cualalitos[i-1].height < piezas[p].rect2[1] + piezas[p].rect2[3]:
                            redrawGameWindow()
                            return True
                elif piezas[p].number == 11:
                    if  piezas[p].rect1[0] < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[p].rect1[0]+ piezas[p].rect1[2]:
                        if  piezas[p].rect1[1] < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[p].rect1[1] + piezas[p].rect1[3]:
                            return True
                    if  piezas[p].rect2[0] < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[p].rect2[0]+ piezas[p].rect2[2]:
                        if  piezas[p].rect2[1] < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[p].rect2[1] + piezas[p].rect2[3]:
                            return True
                    if  piezas[p].rect3[0] < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[p].rect3[0]+ piezas[p].rect3[2]:
                        if  piezas[p].rect3[1] < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[p].rect3[1] + piezas[p].rect3[3]:
                            return True
        else: return False
    #validar posiciones para BackTacking y Programacion dinamica
    def valid_pos_FBT(x, y, j, Cini):
        if(piezas[j].x + piezas[j].width > 900 or piezas[j].y +piezas[j].height > 700):
            return False
        for i in range(16):
            for c in range(piezas[j].cantrect):
                if  piezas[j].rect[c][0] < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[j].rect[c][0]+ piezas[j].rect[c][2]:
                    if  piezas[j].rect[c][1] < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[j].rect[c][1] + piezas[j].rect[c][3]:
                            if plantilla.solv_aux[i] == False:
                                plantilla.solv_aux = Cini.copy()
                                return False
                            plantilla.solv_aux[i] = False   
        return True
    #Crear el cache de Programacion Dinamica
    def Create_cache(x, y, j):
        if(piezas[j].x + piezas[j].width > 900 or piezas[j].y +piezas[j].height > 700):
            return False
        for i in range(16):
            for c in range(piezas[j].cantrect):
                if  piezas[j].rect[c][0] < cualalitos[i].x and cualalitos[i].x + cualalitos[i].width < piezas[j].rect[c][0]+ piezas[j].rect[c][2]:
                    if  piezas[j].rect[c][1] < cualalitos[i].y and cualalitos[i].y + cualalitos[i].height < piezas[j].rect[c][1] + piezas[j].rect[c][3]:
                            if plantilla.solv_aux2[i] == False:
                                return False  
        return True
    #Encontrar alguna pieza que no esté encajada para moverla 
    def find_piece_wo_fit():
        completed = True
        for i in range (3):
            if piezas[i].fited == False:
                return i
        return 5
    #Solucion con programacion Dinamica
    def solve_w_DP():
        pv = ([594, 412], [662, 412], [730, 412], [798, 412], [594, 480], [662, 480], [730, 480], [798, 480],
            [594, 548], [662, 548], [730, 548], [798, 548], [594, 616], [662, 616], [730, 616], [798, 616])
        cache = [[], [], []]
        for n in range (3):
            for rot in range (piezas[n].numgir):
                cache[n].append([])
        def solveDPR():
            Cini = plantilla.solv_aux.copy()
            piece_act = find_piece_wo_fit()
            if piece_act == 5:
                return True
            for g in range(piezas[piece_act].numgir):    
                piezas[piece_act].subnumber = g
                piezas[piece_act].width = pzs[plantilla.CodPieces[dado.number][piece_act]][g].get_width()
                piezas[piece_act].height = pzs[plantilla.CodPieces[dado.number][piece_act]][g].get_height()
                if not cache[piece_act][g]:
                    for i in range(16):
                        piezas[piece_act].x = pv[i][0]
                        piezas[piece_act].y = pv[i][1]
                        redrawGameWindow()
                        if Create_cache(piezas[piece_act].x, piezas[piece_act].y, piece_act):
                            cache[piece_act][g].append(i)
                for i in cache[piece_act][g]:
                    piezas[piece_act].x = pv[i][0]
                    piezas[piece_act].y = pv[i][1]
                    redrawGameWindow()
                    if valid_pos_FBT(piezas[piece_act].x, piezas[piece_act].y, piece_act, Cini):
                        piezas[piece_act].fited = True
                        if solveDPR():
                            return True
                        plantilla.solv_aux = Cini.copy()
                        piezas[piece_act].fited = False
            return False
        return solveDPR()
    #Solucion con Backtracking
    def solve_w_BT():  
        Cini = plantilla.solv_aux.copy()
        pv = ([594,412],[662,412],[730,412],[798,412],[594,480],[662,480],[730,480],[798,480],
            [594,548],[662,548],[730,548],[798,548],[594,616],[662,616],[730,616],[798,616])
        piece_act = find_piece_wo_fit()
        if piece_act == 5:
            return True
        for g in range(piezas[piece_act].numgir):    
            piezas[piece_act].subnumber = g
            piezas[piece_act].width = pzs[plantilla.CodPieces[dado.number][piece_act]][g].get_width()
            piezas[piece_act].height = pzs[plantilla.CodPieces[dado.number][piece_act]][g].get_height()
            for i in range(16):
                piezas[piece_act].x = pv[i][0]
                piezas[piece_act].y = pv[i][1]
                redrawGameWindow()
                if valid_pos_FBT(piezas[piece_act].x, piezas[piece_act].y, piece_act, Cini):
                    piezas[piece_act].fited = True
                    #redrawGameWindow()
                    if solve_w_BT():
                        return True
                    plantilla.solv_aux = Cini.copy()
                    piezas[piece_act].fited = False
        return False
    #Resolver con Fuerza Bruta
    def solve():
        pv = ([594,412],[662,412],[730,412],[798,412],[594,480],[662,480],[730,480],[798,480],
        [594,548],[662,548],[730,548],[798,548],[594,616],[662,616],[730,616],[798,616])
        for girf1 in range (piezas[0].numgir):
            piezas[0].subnumber = girf1
            piezas[0].width = pzs[plantilla.CodPieces[dado.number][0]][girf1].get_width()
            piezas[0].height = pzs[plantilla.CodPieces[dado.number][0]][girf1].get_height()
            for girf2 in range(piezas[1].numgir):
                piezas[1].subnumber = girf2
                piezas[1].width = pzs[plantilla.CodPieces[dado.number][1]][girf2].get_width()
                piezas[1].height = pzs[plantilla.CodPieces[dado.number][1]][girf2].get_height()
                for girf3 in range(piezas[2].numgir):
                        piezas[2].subnumber = girf3
                        piezas[2].width = pzs[plantilla.CodPieces[dado.number][2]][girf3].get_width()
                        piezas[2].height = pzs[plantilla.CodPieces[dado.number][2]][girf3].get_height()
                        for f1 in range(16):
                            piezas[0].x = pv[f1][0]
                            piezas[0].y = pv[f1][1]
                            if (valid_pos(piezas[0].x + piezas[0].width , piezas[0].y +  piezas[0].height,0)):
                                continue
                            for f2 in range(16):
                                piezas[1].x = pv[f2][0]
                                piezas[1].y = pv[f2][1]
                                if (valid_pos(piezas[1].x + piezas[1].width, piezas[1].y + piezas[1].height,1)):
                                    continue
                                for f3 in range(16):
                                    piezas[2].x = pv[f3][0]
                                    piezas[2].y = pv[f3][1]
                                    if (valid_pos(piezas[2].x + piezas[2].width, piezas[2].y + piezas[2].height,2)):
                                        continue
                                    redrawGameWindow()
                                    colision()
                                    if plantilla.Is_solved():
                                        completed = True
                                        return True
    #Escoger poscion
    def Armar(self):
        clock = pygame.time.Clock()
        while self.ChoosePos:  
            clock.tick(27)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:  
                flecha.y += flecha.vel
            if keys[pygame.K_UP]:
                flecha.y -= flecha.vel
            if keys[pygame.K_RETURN]:
                jugador.y = flecha.y -20
                jugadorcpu.visible = True
                jugador.visible = True
                flecha.visible = False
                ChoosePos = False
            self.redrawGameWindow()
        #Inico para el armado   
        while run:
            clock.tick(27)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
        #PARA LANZAR EL DADO Y SELECCION DE FICHAS
                elif event.type == pygame.MOUSEBUTTONUP:
                            pos = pygame.mouse.get_pos()
                            if dado.hitbox[0] < pos[0] and pos[0] < dado.hitbox[0] + dado.hitbox[2]:
                                if dado.hitbox[1] < pos[1] and pos[1] < dado.hitbox[1] + dado.hitbox[3]:
                                    dado.number = 1
                                    #dado.ThrowDice()
                                    dado.throwed = True
                                    cuadrado.y = cuadrado.yini + ((cuadrado.height * dado.number)+(dado.number* 13.5))
                                    for i in range(3):    
                                        piezas.append(pieces(594 , 412, pzs[plantilla.CodPieces[dado.number][i]][0].get_width() , pzs[plantilla.CodPieces[dado.number][i]][0].get_height(), plantilla.CodPieces[dado.number][i]))
                                    piezas[0].visible = True
                            #Para seleccionar la ficha p
                            if cuadrado.y < pos[1] and pos[1] < cuadrado.y + cuadrado.height:
                                if cuadrado.x < pos[0] and pos[0] < cuadrado.x + cuadrado.width:
                                    cuadrado.visible1 = True
                                    cuadrado.visible2 = False
                                    cuadrado.visible3 = False
                                    self.PieceSelect = 0
                                if cuadrado.x + cuadrado.width< pos[0] and pos[0] < cuadrado.x + (cuadrado.width*2):
                                    cuadrado.visible2 = True
                                    cuadrado.visible1 = False
                                    cuadrado.visible3 = False
                                    piezas[1].visible = True
                                    self.PieceSelect = 1
                                if cuadrado.x + (cuadrado.width*2)< pos[0] and pos[0] < cuadrado.x + (cuadrado.width*3):
                                    cuadrado.visible3 = True
                                    cuadrado.visible2 = False
                                    cuadrado.visible1 = False
                                    piezas[2].visible = True
                                    self.PieceSelect = 2

        #Colission piezas plantilla y armarse_cpu
            if dado.throwed:
                colision()
            if plantilla.Is_solved():
                completed = True
            if pls == 0:
                if solve_w_DP():
                    completed = True
                pls = 1
            if asd == -1:
                solve()
                asd = 1
        #MIVIMIENTO DE FICHAS
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                piezas[PieceSelect].move_down()
            if keys[pygame.K_UP]:
                piezas[PieceSelect].move_up()
            if keys[pygame.K_RIGHT]:
                piezas[PieceSelect].move_right()
            if keys[pygame.K_LEFT]:
                piezas[PieceSelect].move_left()
            #rotar fichas
            if keys[pygame.K_SPACE]:
                piezas[PieceSelect].subnumber = piezas[PieceSelect].subnumber +1
            if piezas[PieceSelect].subnumber > 3:
                piezas[PieceSelect].subnumber = 0
            piezas[PieceSelect].width = pzs[plantilla.CodPieces[dado.number][PieceSelect]][piezas[PieceSelect].subnumber].get_width()
            piezas[PieceSelect].height = pzs[plantilla.CodPieces[dado.number][PieceSelect]][piezas[PieceSelect].subnumber].get_height()
            self.redrawGameWindow()
        pygame.quit()


def Start():
    portada