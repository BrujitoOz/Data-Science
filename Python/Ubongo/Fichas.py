import pygame

pzs =  [[[(pygame.image.load('ficha1.png')), (pygame.image.load('ficha1_1.png')),(pygame.image.load('ficha1.png')), (pygame.image.load('ficha1_1.png'))],
       [(pygame.image.load('ficha2.png')), (pygame.image.load('ficha2_1.png')),(pygame.image.load('ficha2.png')), (pygame.image.load('ficha2_1.png'))],
       [(pygame.image.load('ficha3.png')), (pygame.image.load('ficha3_1.png')),(pygame.image.load('ficha3.png')), (pygame.image.load('ficha3_1.png'))], 
       [(pygame.image.load('ficha4.png')), (pygame.image.load('ficha4.png')),(pygame.image.load('ficha4.png')), (pygame.image.load('ficha4.png'))],
       [(pygame.image.load('ficha5.png')), (pygame.image.load('ficha5_1.png')),(pygame.image.load('ficha5_2.png')), (pygame.image.load('ficha5_3.png'))],
       [(pygame.image.load('ficha6.png')), (pygame.image.load('ficha6_1.png')),(pygame.image.load('ficha6_2.png')), (pygame.image.load('ficha6_3.png'))], 
       [(pygame.image.load('ficha7_0_1.png')), (pygame.image.load('ficha7_1_1.png')),(pygame.image.load('ficha7_2_1.png')), (pygame.image.load('ficha7_3_1.png'))],
       [(pygame.image.load('ficha8.png')), (pygame.image.load('ficha8_1.png')),(pygame.image.load('ficha8.png')), (pygame.image.load('ficha8_1.png'))],
       [(pygame.image.load('ficha9.png')), (pygame.image.load('ficha9_1.png')),(pygame.image.load('ficha9_2.png')), (pygame.image.load('ficha9_3.png'))], 
       [(pygame.image.load('ficha10.png')), (pygame.image.load('ficha10_1.png')),(pygame.image.load('ficha10_2.png')), (pygame.image.load('ficha10_3.png'))],
       [(pygame.image.load('ficha11.png')), (pygame.image.load('ficha11_1.png')),(pygame.image.load('ficha11_2.png')), (pygame.image.load('ficha11_3.png'))],
       [(pygame.image.load('ficha12.png')), (pygame.image.load('ficha12_1.png')),(pygame.image.load('ficha12.png')), (pygame.image.load('ficha12_1.png'))]],
       [[(pygame.image.load('ficha1.png')), (pygame.image.load('ficha1_1.png')),(pygame.image.load('ficha1.png')), (pygame.image.load('ficha1_1.png'))],
       [(pygame.image.load('ficha2.png')), (pygame.image.load('ficha2_1.png')),(pygame.image.load('ficha2.png')), (pygame.image.load('ficha2_1.png'))],
       [(pygame.image.load('ficha3.png')), (pygame.image.load('ficha3_1.png')),(pygame.image.load('ficha3.png')), (pygame.image.load('ficha3_1.png'))], 
       [(pygame.image.load('ficha4.png')), (pygame.image.load('ficha4.png')),(pygame.image.load('ficha4.png')), (pygame.image.load('ficha4.png'))],
       [(pygame.image.load('ficha5.png')), (pygame.image.load('ficha5_1.png')),(pygame.image.load('ficha5_2.png')), (pygame.image.load('ficha5_3.png'))],
       [(pygame.image.load('ficha6.png')), (pygame.image.load('ficha6_1.png')),(pygame.image.load('ficha6_2.png')), (pygame.image.load('ficha6_3.png'))], 
       [(pygame.image.load('ficha7.png')), (pygame.image.load('ficha7_1.png')),(pygame.image.load('ficha7_2.png')), (pygame.image.load('ficha7_3.png'))],
       [(pygame.image.load('ficha8_v1.png')), (pygame.image.load('ficha8_v2.png')),(pygame.image.load('ficha8_v1.png')), (pygame.image.load('ficha8_v2.png'))],
       [(pygame.image.load('ficha9_v1.png')), (pygame.image.load('ficha9_v2.png')),(pygame.image.load('ficha9_v3.png')), (pygame.image.load('ficha9_v4.png'))], 
       [(pygame.image.load('ficha10_v1.png')), (pygame.image.load('ficha10_v2.png')),(pygame.image.load('ficha10_v3.png')), (pygame.image.load('ficha10_v4.png'))],
       [(pygame.image.load('ficha11_v1.png')), (pygame.image.load('ficha11_v2.png')),(pygame.image.load('ficha11_v3.png')), (pygame.image.load('ficha11_v4.png'))],
       [(pygame.image.load('ficha12_v1.png')), (pygame.image.load('ficha12_v2.png')),(pygame.image.load('ficha12_v1.png')), (pygame.image.load('ficha12_v2.png'))]]]

class pieces(object):
    def __init__(self, x, y, width, height, number):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 34
        self.number = number
        self.fited = False
        self.subnumber = 0
        self.numgir = 0
        self.visible = True
        self.cantrect = 0
        self.cantver = 0
        self.version = 0
        self.how_gir()
        self.how_rects()
        self.how_ver()
        self.rect = [0, 0, 0, 0] * self.cantrect
        self.rect2 = [0, 0, 0, 0] * self.cantrect
        self.create_rect_col()
        self.create_rect2_col()

    def how_ver(self):
        if self.number > 5:
            self.cantver = 2
        else:
            self.cantver = 1
    def how_gir(self):
        if self.number < 3: self.numgir = 2
        elif self.number == 3: self.numgir = 1
        elif self.number == 7 or self.number == 11: self.numgir = 2
        else: self.numgir = 4
    def how_rects(self):
        if self.number <= 3: self.cantrect = 1
        elif self.number < 11: self.cantrect = 2
        else: self.cantrect = 3
    def draw(self, win):
        if self.visible:
            win.blit(pzs[self.version][self.number][self.subnumber], (self.x, self.y))

    def move_down(self):
        self.y += self.vel
    def move_up(self):
        self.y -= self.vel
    def move_right(self):
        self.x += self.vel
    def move_left(self):
        self.x -= self.vel
    def Puzzle_Assemble(self):
        pass
    def Valid_pos(self):
        if self.x <= 764 and self.y <= 611:
            return True
        return False
    def create_rect_col(self):
        if self.number <= 3:
            self.rect[0] = [self.x+10, self.y+10, self.width-20, self.height-20]
        elif self.number == 4:
            self.rect[0] = [self.x, self.y, (self.width/2), self.height]
            self.rect[1] = [self.x + (self.width/2), self.y + (self.height/2), (self.width/2), (self.height /2)] 
        elif self.number == 5:
            self.rect[0] = [self.x, self.y, (self.width/2), (self.height)]
            self.rect[1] = [(self.x + (self.width/2)), self.y + (self.height/3), (self.width/2), (self.height /3)]
        elif self.number == 6:
            self.rect[0] = [self.x, self.y, (self.width/3), (self.height/2)]
            self.rect[1] = [(self.x), self.y + (self.height/2), (self.width), (self.height /2)]
        elif self.number == 7:
            self.rect[0] = [self.x, self.y, (self.width/2), (self.height/3)*2]
            self.rect[1] = [self.x + (self.width/2), self.y + (self.height/3), (self.width/2), (self.height /3)*2]
        elif self.number == 8:
            self.rect[0] = [self.x , self.y, (self.width/2), self.height]
            self.rect[1] = [self.x +(self.width/2)  , self.y , (self.width/2), (self.height /4 )]
        elif self.number == 9:
            self.rect[0] = [self.x , self.y, (self.width/2), self.height]
            self.rect[1] = [self.x +(self.width/2)  , self.y , (self.width/2), (self.height /4 )]
        elif self.number == 10:
            self.rect[0] = [self.x , self.y, (self.width*2/3), self.height/2]
            self.rect[1] = [self.x   , self.y +(self.height /2 ), (self.width), (self.height /2 )]
        elif self.number == 11:
            self.rect[0] = [self.x , self.y, (self.width/3), (self.height/3)]
            self.rect[1] = [self.x +(self.width/3)  , self.y , (self.width/3), (self.height)]
            self.rect[2] = [self.x +((self.width/3)*2)  , self.y + ((self.width/3)*2) , (self.width/3), (self.height /3 )]
    def create_rect2_col(self):   
            if self.number <=3:
                self.rect2[0] = [self.x, self.y, self.width, self.height]
            elif self.number == 4:
                self.rect2[0] = [self.x , self.y, (self.width/2), self.height]
                self.rect2[1] = [self.x + (self.width/2) , self.y + (self.height/2), (self.width/2), (self.height /2 )]  
            elif self.number == 5:
                self.rect2[0] = [self.x , self.y, (self.width/2), (self.height)]
                self.rect2[1] = [(self.x + (self.width/2)) , self.y + (self.height/3), (self.width/2), (self.height /3 )]
            elif self.number == 6:
                self.rect2[0] = [self.x , self.y, (self.width/3), (self.height/2)]
                self.rect2[1] = [(self.x ) , self.y + (self.height/2), (self.width), (self.height /2 )]
            elif self.number == 7:
                self.rect2[0] = [self.x , self.y, (self.width/2), (self.height/3)*2]
                self.rect2[1] = [self.x + (self.width/2), self.y + (self.height/3),   (self.width/2), (self.height /3 )*2]
            elif self.number == 8:
                self.rect2[0] = [self.x , self.y, (self.width/2), self.height]
                self.rect2[1] = [self.x +(self.width/2)  , self.y , (self.width/2), (self.height /4 )]
            elif self.number == 9:
                self.rect2[0] = [self.x , self.y, (self.width/2), self.height]
                self.rect2[1] = [self.x +(self.width/2)  , self.y , (self.width/2), (self.height /4 )]
            elif self.number == 10:
                self.rect2[0] = [self.x , self.y, (self.width*2/3), self.height/2]
                self.rect2[1] = [self.x   , self.y +(self.height /2 ), (self.width), (self.height /2 )]
            elif self.number == 11:
                self.rect2[0] = [self.x , self.y, (self.width/3), (self.height/3)]
                self.rect2[1] = [self.x +(self.width/3)  , self.y , (self.width/3), (self.height)]
                self.rect2[2] = [self.x +((self.width/3)*2)  , self.y + ((self.width/3)*2) , (self.width/3), (self.height /3 )]

    def draw_rect_col(self, win):
        if self.number <= 3:
            self.rect[0] = [self.x+10, self.y+10, self.width-20, self.height-20]
            #pygame.draw.rect(win, (0,0,255), self.rect[0] ,2)
        else:
            if self.number == 4:
                if self.subnumber == 0:
                    self.rect[0] = [self.x +10, self.y+10, (self.width/2)-20, self.height-20]
                    self.rect[1] = [self.x + 10+(self.width/2) , self.y+10 + (self.height/2), (self.width/2)-20, (self.height /2 )-20]    
                elif self.subnumber == 1:
                    self.rect[0] = [self.x +10, self.y+10, (self.width)-20, self.height/2-20]
                    self.rect[1] = [self.x+10 , self.y + (self.height/2)+10, (self.width/2-20), (self.height /2-20 )] 
                elif self.subnumber == 2:
                    self.rect[0] = [self.x +10, self.y+10, (self.width)-20, self.height/2-20]
                    self.rect[1] = [self.x + 10+(self.width/2) , self.y +10+ (self.height/2), (self.width/2)-20, (self.height /2 )-20]    
                elif self.subnumber == 3:
                    self.rect[0] = [self.x + (self.width/2)+10, self.y+10, (self.width/2)-20, self.height/2 -20]
                    self.rect[1] = [self.x +10 , self.y + (self.height/2)+10, (self.width)-20, (self.height /2 )-20]
                #pygame.draw.rect(win, (0,0,255), (self.rect[0]) ,2)
                #pygame.draw.rect(win, (0,0,255), (self.rect[1]) ,2)
            elif self.number == 5:
                if self.subnumber == 0:
                    self.rect[0] = [self.x +10, self.y+10, (self.width/2)-20, self.height-20]
                    self.rect[1] = [self.x +10+ (self.width/2) , 10+self.y + (self.height/3), (self.width/2)-20, (self.height /3 )-20]    
                elif self.subnumber == 1:
                    self.rect[0] = [self.x+10 , self.y+10, (self.width)-20, self.height/2-20]
                    self.rect[1] = [self.x +10+ (self.width/3),10+ self.y + (self.height/2), (self.width/3)-20, (self.height /2 )-20] 
                elif self.subnumber == 2:
                    self.rect[0] = [self.x +10, self.y + (self.height/3)+10, (self.width/2)-20, self.height/3-20]
                    self.rect[1] = [self.x + 10+(self.width/2) , self.y +10, (self.width/2)-20, (self.height)-20]    
                elif self.subnumber == 3:
                    self.rect[0] = [self.x + (self.width/3)+10, self.y+10, (self.width/3)-20, self.height/2-20 ]
                    self.rect[1] = [self.x +10 , self.y +10+ (self.height/2), (self.width)-20, (self.height /2 )-20]
                #pygame.draw.rect(win, (0,0,255), (self.rect[0]) ,2)
                #pygame.draw.rect(win, (0,0,255), (self.rect[1]) ,2)
            elif self.number == 6:
                if self.version == 0:
                    if self.subnumber == 0:
                        self.rect[0] = [self.x+10 , self.y+10, (self.width)-20, (self.height/2)-20]
                        self.rect[1] = (self.x  +10, self.y + (self.height/2)+10, (self.width/3)-20, (self.height /2 )-20)
                    elif self.subnumber == 1:
                        self.rect[0] = [self.x +10, self.y+10, (self.width/2)-20, (self.height/3)-20]
                        self.rect[1] = (self.x +(self.width/2) +10, self.y +10, (self.width/2)-20, (self.height )-20)
                    elif self.subnumber == 2:
                        self.rect[0] = [self.x + ((self.width/3)*2) +10, self.y+10, (self.width/3)-20, (self.height/2)-20]
                        self.rect[1] = (self.x +10 , self.y + (self.height/2)+10, (self.width)-20, (self.height/2 )-20)
                    elif self.subnumber == 3:
                        self.rect[0] = [self.x +10, self.y+10, (self.width/2)-20, (self.height)-10]
                        self.rect[1] = (self.x +(self.width/2)+10 , self.y + (self.height*2/3)+10, (self.width/2)-20, (self.height /3 )-20)
                else: 
                    if self.subnumber == 0:
                        self.rect[0] = [self.x+10 , self.y+10, (self.width/3)-20, (self.height/2)-20]
                        self.rect[1] = (self.x  +10, self.y + (self.height/2)+10, (self.width)-20, (self.height /2 )-20)
                    elif self.subnumber == 1:
                        self.rect[0] = [self.x +10, self.y+10, (self.width/2)-20, (self.height)-20]
                        self.rect[1] = (self.x +(self.width/2) +10, self.y +10, (self.width/2)-20, (self.height/3 )-20)
                    elif self.subnumber == 2:
                        self.rect[0] = [self.x  +10, self.y+10, (self.width)-20, (self.height/2)-20]
                        self.rect[1] = (self.x +10 + ((self.width/3)*2) , self.y + (self.height/2)+10, (self.width/3)-20, (self.height/2 )-20)
                    elif self.subnumber == 3:
                        self.rect[0] = [self.x + 10, self.y + (self.height*2/3)+10, (self.width/2)-20, (self.height/3)-10]
                        self.rect[1] = (self.x +(self.width/2)+10 , self.y +10, (self.width/2)-20, (self.height )-20)
                #pygame.draw.rect(win, (0,0,255), (self.rect[0]) ,2)
                #pygame.draw.rect(win, (0,0,255), (self.rect[1]) ,2)
            elif self.number == 7:
                if self.version == 0:
                    if self.subnumber == 0 or self.subnumber == 2 :
                        self.rect[0] = [self.x +10, self.y+10, (self.width/2)-20, (self.height/3)*2-20]
                        self.rect[1] = (self.x + (self.width/2)+10, self.y + (self.height/3)+10,   (self.width/2)-20, (self.height /3 )*2-20)
                    elif self.subnumber == 1 or self.subnumber == 3:
                        self.rect[0] = [self.x+(self.width/3) +10, self.y+10, (self.width*2/3)-20, (self.height/2)-20]
                        self.rect[1] = (self.x+10 , self.y + (self.height/2)+10,   (self.width*2/3)-20, (self.height /2 )-20)
                else: 
                    if self.subnumber == 0 or self.subnumber == 2 :
                        self.rect[0] = [self.x + (self.width/2)+10, self.y+10, (self.width/2)-20, (self.height/3)*2-20]
                        self.rect[1] = (self.x +10, self.y + (self.height/3)+10,   (self.width/2)-20, (self.height /3 )*2-20)
                    elif self.subnumber == 1 or self.subnumber == 3:
                        self.rect[0] = [self.x +10, self.y+10, (self.width*2/3)-20, (self.height/2)-20]
                        self.rect[1] = (self.x +(self.width/3)+10 , self.y + (self.height/2)+10,   (self.width*2/3)-20, (self.height /2 )-20)
                #pygame.draw.rect(win, (0,0,255), (self.rect[0]) ,2)
                #pygame.draw.rect(win, (0,0,255), (self.rect[1]) ,2)
            elif self.number == 8:
                if self.version == 0:
                    if self.subnumber == 0:
                        self.rect[0] = [self.x +10, self.y+10, (self.width/2)-20, self.height-20]
                        self.rect[1] = [self.x +(self.width/2) +10 , self.y+10 , (self.width/2)-20, (self.height /4 )-20]
                    elif self.subnumber == 1:
                        self.rect[0] = [self.x +10, self.y+10, (self.width)-20, self.height/2-20]
                        self.rect[1] = [self.x +((self.width/4)*3) +10 , self.y + 10+(self.height /2 ) , (self.width/4)-20, (self.height /2 )-20]
                    elif self.subnumber == 2:
                        self.rect[0] = [self.x +10, self.y + (self.height*3/4)+10, (self.width/2)-20, self.height/4-20]
                        self.rect[1] = [self.x +(self.width/2) +10 , self.y+10  , (self.width/2)-20, (self.height )-20]
                    elif self.subnumber == 3:
                        self.rect[0] = [self.x +10, self.y+10, (self.width/4)-20, self.height/2-20]
                        self.rect[1] = [self.x   +10, self.y +10+ (self.height /2 ) , (self.width)-20, (self.height /2 )-20]
                else:
                    if self.subnumber == 0:
                        self.rect[0] = [self.x +10, self.y+10, (self.width/2)-20, (self.height/4)-20]
                        self.rect[1] = [self.x +(self.width/2) +10 , self.y+10 , (self.width/2)-20, (self.height)-20]
                    elif self.subnumber == 1:
                        self.rect[0] = [self.x +10, self.y + (self.height /2 )+10 , (self.width)-20, self.height/2-20]
                        self.rect[1] = [self.x +((self.width/4)*3) +10 , self.y + 10 , (self.width/4)-20, (self.height /2 )-20]
                    elif self.subnumber == 2:
                        self.rect[0] = [self.x +10, self.y +10, (self.width/2)-20, self.height-20]
                        self.rect[1] = [self.x +(self.width/2) +10 , self.y + (self.height*3/4)+10  , (self.width/2)-20, (self.height/4 )-20]
                    elif self.subnumber == 3:
                        self.rect[0] = [self.x +10, self.y+10, (self.width)-20, self.height/2-20]
                        self.rect[1] = [self.x   +10, self.y +10+ (self.height /2 ) , (self.width/4)-20, (self.height /2 )-20]
                #pygame.draw.rect(win, (0,0,255), (self.rect[0]) ,2)
                #pygame.draw.rect(win, (0,0,255), (self.rect[1]) ,2)
            elif self.number == 9:
                if self.version == 0:
                    if self.subnumber == 0:
                        self.rect[0] = [self.x +10, self.y+10, (self.width/2)-20, self.height-20]
                        self.rect[1] = [self.x +(self.width/2) +10 , self.y + (self.height /4 )+10, (self.width/2)-20, (self.height /4 )-20]
                    elif self.subnumber == 1:
                        self.rect[0] = [self.x +10, self.y+10, (self.width)-20, self.height/2-20]
                        self.rect[1] = [self.x +((self.width/4)*2) +10 , self.y+10 + (self.height /2 ) , (self.width/4)-20, (self.height /2 )-20]
                    elif self.subnumber == 2:
                        self.rect[0] = [self.x +10, self.y + (self.height*2/4)+10, (self.width/2)-20, self.height/4-20]
                        self.rect[1] = [self.x +(self.width/2) +10 , self.y +10 , (self.width/2)-20, (self.height )-20]
                    elif self.subnumber == 3:
                        self.rect[0] = [self.x + (self.width/4)+10, self.y+10, (self.width/4)-20, self.height/2-20]
                        self.rect[1] = [self.x +10, self.y + (self.height /2 ) +10, (self.width)-20, (self.height /2 )-20]
                else:
                    if self.subnumber == 0:
                        self.rect[0] = [self.x +(self.width/2)+10, self.y+10, (self.width/2)-20, self.height-20]
                        self.rect[1] = [self.x  +10 , self.y + (self.height /4 )+10, (self.width/2)-20, (self.height /4 )-20]
                    elif self.subnumber == 1:
                        self.rect[0] = [self.x +((self.width/4)*2)+10, self.y+10, (self.width/4)-20, self.height/2-20]
                        self.rect[1] = [self.x  +10 , self.y+10 + (self.height /2 ) , (self.width)-20, (self.height /2 )-20]
                    elif self.subnumber == 2:
                        self.rect[0] = [self.x +10, self.y +10, (self.width/2)-20, self.height-20]
                        self.rect[1] = [self.x +(self.width/2) +10 , self.y + (self.height*2/4) +10 , (self.width/2)-20, (self.height/4)-20]
                    elif self.subnumber == 3:
                        self.rect[0] = [self.x +10, self.y+10, (self.width)-20, self.height/2-20]
                        self.rect[1] = [self.x + (self.width/4)+10, self.y + (self.height /2 ) +10, (self.width/4)-20, (self.height /2 )-20]
                #pygame.draw.rect(win, (0,0,255), (self.rect[0]) ,2)
                #pygame.draw.rect(win, (0,0,255), (self.rect[1]) ,2)
            elif self.number == 10:
                if self.version == 0:
                    if self.subnumber == 0:
                        self.rect[0] = [self.x +10, self.y+10, (self.width*2/3)-20, self.height/2-20]
                        self.rect[1] = [self.x   +10, self.y +10+(self.height /2 ), (self.width)-20, (self.height /2 )-20]
                    elif self.subnumber == 1:
                        self.rect[0] = [self.x+10 ,10+ self.y, (self.width)-20, self.height*2/3-20]
                        self.rect[1] = [self.x +10  , self.y +10+ (self.height *2/3 ) , (self.width/2)-20, (self.height /3 )-20]
                    elif self.subnumber == 2:
                        self.rect[0] = [self.x +10, self.y+10, (self.width)-20, self.height/2-20]
                        self.rect[1] = [self.x +((self.width/3))  +10, self.y + (self.height /2 )+10 , (self.width*2/3)-20, (self.height /2 )-20]
                    elif self.subnumber == 3:
                        self.rect[0] = [self.x +(self.width/2)+10 , self.y+10, (self.width/2)-20, self.height/3-20]
                        self.rect[1] = [self.x  +10 , self.y + (self.height /3 ) +10, (self.width)-20, (self.height*2/3 )-20]
                else:
                    if self.subnumber == 0:
                        self.rect[0] = [self.x +10, self.y+10, (self.width)-20, self.height/2-20]
                        self.rect[1] = [self.x   +10, self.y +10+(self.height /2 ), (self.width*2/3)-20, (self.height /2 )-20]
                    elif self.subnumber == 1:
                        self.rect[0] = [self.x+10 ,10+ self.y, (self.width/2)-20, self.height-20]
                        self.rect[1] = [self.x +10 +(self.width/2) , self.y +10+ (self.height/3 ) , (self.width/2)-20, (self.height*2/3 )-20]
                    elif self.subnumber == 2:
                        self.rect[0] = [self.x + ((self.width/3)) +10, self.y+10, (self.width*2/3)-20, self.height/2-20]
                        self.rect[1] = [self.x + +10, self.y + (self.height /2 )+10 , (self.width)-20, (self.height /2 )-20]
                    elif self.subnumber == 3:
                        self.rect[0] = [self.x +(self.width/2)+10 , self.y+10, (self.width/2)-20, self.height-20]
                        self.rect[1] = [self.x  +10 , self.y  +10, (self.width/2)-20, (self.height*2/3 )-20]
                #pygame.draw.rect(win, (0,0,255), (self.rect[0]) ,2)
                #pygame.draw.rect(win, (0,0,255), (self.rect[1]) ,2)
            elif self.number == 11:
                if self.version == 0:
                    if self.subnumber == 0 or  self.subnumber == 2:
                        self.rect[0] = [self.x +10, self.y + 10, (self.width/3) -20, (self.height/3) -20] 
                        self.rect[1] = [self.x +(self.width/3) +10 , self.y +10, (self.width/3)-20, (self.height)-20]
                        self.rect[2] = [self.x +((self.width/3)*2) +10 , self.y +10+ ((self.width/3)*2) , (self.width/3)-20, (self.height /3 )-20]
                    elif self.subnumber == 1 or  self.subnumber == 3:
                        self.rect[0] = [self.x +10, self.y + (self.height/3)+10, (self.width/3)-20, (self.height*2/3)-20]
                        self.rect[1] = [self.x +10+(self.width/3)  , self.y + 10+(self.height/3), (self.width/3)-20, (self.height/3)-20]
                        self.rect[2] = [self.x +10+((self.width/3)*2)  , self.y +10, (self.width/3)-20, (self.height*2/3 )-20]
                else:
                    if self.subnumber == 0 or  self.subnumber == 2:
                        self.rect[0] = [self.x +10, self.y+((self.width/3)*2) + 10, (self.width/3) -20, (self.height/3) -20] 
                        self.rect[1] = [self.x +(self.width/3) +10 , self.y +10, (self.width/3)-20, (self.height)-20]
                        self.rect[2] = [self.x +((self.width/3)*2) +10 , self.y +10 , (self.width/3)-20, (self.height /3 )-20]
                    elif self.subnumber == 1 or  self.subnumber == 3:
                        self.rect[0] = [self.x +10, self.y +10, (self.width/3)-20, (self.height*2/3)-20]
                        self.rect[1] = [self.x +10+(self.width/3)  , self.y + 10+(self.height/3), (self.width/3)-20, (self.height/3)-20]
                        self.rect[2] = [self.x +10+((self.width/3)*2)  , self.y +10 + (self.height/3), (self.width/3)-20, (self.height*2/3 )-20]
                #pygame.draw.rect(win, (0,0,255), (self.rect[0]) ,2)
                #pygame.draw.rect(win, (0,0,255), (self.rect[1]) ,2)
                #pygame.draw.rect(win, (0,0,255), (self.rect[2]) ,2)
    def draw_rect2_col(self, win):
        if self.number <= 3:
            self.rect2[0] = [self.x, self.y, self.width, self.height]
            pygame.draw.rect(win, (255,0,0), self.rect2[0] ,2)
        else:
            if self.number == 4:
                if self.subnumber == 0:
                    self.rect2[0] = [self.x , self.y, (self.width/2), self.height]
                    self.rect2[1] = [self.x +(self.width/2) , self.y + (self.height/2), (self.width/2), (self.height /2 )]    
                elif self.subnumber == 1:
                    self.rect2[0] = [self.x , self.y, (self.width), self.height/2]
                    self.rect2[1] = [self.x , self.y + (self.height/2), (self.width/2), (self.height /2 )] 
                elif self.subnumber == 2:
                    self.rect2[0] = [self.x , self.y, (self.width), self.height/2]
                    self.rect2[1] = [self.x +(self.width/2) , self.y + (self.height/2), (self.width/2), (self.height /2 )]    
                elif self.subnumber == 3:
                    self.rect2[0] = [self.x + (self.width/2), self.y, (self.width/2), self.height/2 ]
                    self.rect2[1] = [self.x +10 , self.y + (self.height/2), (self.width), (self.height /2 )]
                pygame.draw.rect(win, (255,0,0), (self.rect2[0]) ,2)
                pygame.draw.rect(win, (255,0,0), (self.rect2[1]) ,2)
            elif self.number == 5:
                if self.subnumber == 0:
                    self.rect2[0] = [self.x , self.y, (self.width/2), self.height]
                    self.rect2[1] = [self.x + (self.width/2) , self.y + (self.height/3), (self.width/2), (self.height /3 )]    
                elif self.subnumber == 1:
                    self.rect2[0] = [self.x , self.y, (self.width), self.height/2]
                    self.rect2[1] = [self.x + (self.width/3), self.y + (self.height/2), (self.width/3), (self.height /2 )] 
                elif self.subnumber == 2:
                    self.rect2[0] = [self.x , self.y + (self.height/3), (self.width/2), self.height/3]
                    self.rect2[1] = [self.x +(self.width/2) , self.y , (self.width/2), (self.height)]    
                elif self.subnumber == 3:
                    self.rect2[0] = [self.x + (self.width/3), self.y, (self.width/3), self.height/2 ]
                    self.rect2[1] = [self.x  , self.y + (self.height/2), (self.width), (self.height /2 )]
                pygame.draw.rect(win, (255,0,0), (self.rect2[0]) ,2)
                pygame.draw.rect(win, (255,0,0), (self.rect2[1]) ,2)
            elif self.number == 6:
                if self.subnumber == 0:
                    self.rect2[0] = [self.x , self.y, (self.width), (self.height/2)]
                    self.rect2[1] = (self.x  , self.y + (self.height/2), (self.width/3), (self.height /2 ))
                elif self.subnumber == 1:
                    self.rect2[0] = [self.x , self.y, (self.width/2), (self.height/3)]
                    self.rect2[1] = (self.x +(self.width/2) , self.y , (self.width/2), (self.height ))
                elif self.subnumber == 2:
                    self.rect2[0] = [self.x + ((self.width/3)*2) , self.y, (self.width/3), (self.height/2)]
                    self.rect2[1] = (self.x , self.y + (self.height/2), (self.width), (self.height/2 ))
                elif self.subnumber == 3:
                    self.rect2[0] = [self.x , self.y, (self.width/2), (self.height)]
                    self.rect2[1] = (self.x +(self.width/2) , self.y + (self.height*2/3), (self.width/2), (self.height /3 ))
                pygame.draw.rect(win, (255,0,0), (self.rect2[0]) ,2)
                pygame.draw.rect(win, (255,0,0), (self.rect2[1]) ,2)
            elif self.number == 7:
                if self.subnumber == 0 or self.subnumber == 2 :
                    self.rect2[0] = [self.x , self.y, (self.width/2), (self.height/3)*2]
                    self.rect2[1] = (self.x + (self.width/2), self.y + (self.height/3),   (self.width/2), (self.height /3 )*2)
                elif self.subnumber == 1 or self.subnumber == 3:
                    self.rect2[0] = [self.x+(self.width/3) , self.y, (self.width*2/3), (self.height/2)]
                    self.rect2[1] = (self.x, self.y + (self.height/2),   (self.width*2/3), (self.height /2 ))
                pygame.draw.rect(win, (255,0,0), (self.rect2[0]) ,2)
                pygame.draw.rect(win, (255,0,0), (self.rect2[1]) ,2)
            elif self.number == 8:
                if self.subnumber == 0:
                    self.rect2[0] = [self.x , self.y, (self.width/2), self.height]
                    self.rect2[1] = [self.x +(self.width/2) , self.y , (self.width/2), (self.height /4 )]
                elif self.subnumber == 1:
                    self.rect2[0] = [self.x , self.y, (self.width), self.height/2]
                    self.rect2[1] = [self.x +((self.width/4)*3)  , self.y +(self.height /2 ) , (self.width/4), (self.height /2 )]
                elif self.subnumber == 2:
                    self.rect2[0] = [self.x , self.y + (self.height*3/4), (self.width/2), self.height/4]
                    self.rect2[1] = [self.x +(self.width/2)  , self.y  , (self.width/2), (self.height )]
                elif self.subnumber == 3:
                    self.rect2[0] = [self.x , self.y, (self.width/4), self.height/2]
                    self.rect2[1] = [self.x  , self.y + (self.height /2 ) , (self.width), (self.height /2 )]
                pygame.draw.rect(win, (255,0,0), (self.rect2[0]) ,2)
                pygame.draw.rect(win, (255,0,0), (self.rect2[1]) ,2)
            elif self.number == 9:
                if self.subnumber == 0:
                    self.rect2[0] = [self.x , self.y, (self.width/2), self.height]
                    self.rect2[1] = [self.x +(self.width/2) , self.y + (self.height /4 ), (self.width/2), (self.height /4 )]
                elif self.subnumber == 1:
                    self.rect2[0] = [self.x , self.y, (self.width), self.height/2]
                    self.rect2[1] = [self.x +((self.width/4)*2)  , self.y + (self.height /2 ) , (self.width/4), (self.height /2 )]
                elif self.subnumber == 2:
                    self.rect2[0] = [self.x , self.y + (self.height*2/4), (self.width/2), self.height/4]
                    self.rect2[1] = [self.x +(self.width/2)  , self.y  , (self.width/2), (self.height )]
                elif self.subnumber == 3:
                    self.rect2[0] = [self.x + (self.width/4), self.y, (self.width/4), self.height/2]
                    self.rect2[1] = [self.x , self.y + (self.height /2 ) , (self.width), (self.height /2 )]
                pygame.draw.rect(win, (255,0,0), (self.rect2[0]) ,2)
                pygame.draw.rect(win, (255,0,0), (self.rect2[1]) ,2)
            elif self.number == 10:
                if self.subnumber == 0:
                    self.rect2[0] = [self.x , self.y, (self.width*2/3), self.height/2]
                    self.rect2[1] = [self.x  , self.y +(self.height /2 ), (self.width), (self.height /2 )]
                elif self.subnumber == 1:
                    self.rect2[0] = [self.x , self.y, (self.width), self.height*2/3]
                    self.rect2[1] = [self.x   , self.y + (self.height *2/3 ) , (self.width/2), (self.height /3 )]
                elif self.subnumber == 2:
                    self.rect2[0] = [self.x , self.y, (self.width), self.height/2]
                    self.rect2[1] = [self.x +((self.width/3))  , self.y + (self.height /2 ) , (self.width*2/3), (self.height /2 )]
                elif self.subnumber == 3:
                    self.rect2[0] = [self.x +(self.width/2) , self.y, (self.width/2), self.height/3]
                    self.rect2[1] = [self.x  , self.y + (self.height /3 ) , (self.width), (self.height*2/3 )]
                pygame.draw.rect(win, (255,0,0), (self.rect2[0]) ,2)
                pygame.draw.rect(win, (255,0,0), (self.rect2[1]) ,2)
            elif self.number == 11:
                if self.subnumber == 0 or  self.subnumber == 2:
                    self.rect2[0] = [self.x , self.y , (self.width/3) , (self.height/3) ] 
                    self.rect2[1] = [self.x +(self.width/3)  , self.y, (self.width/3), (self.height)]
                    self.rect2[2] = [self.x +((self.width/3)*2)  , self.y + ((self.width/3)*2) , (self.width/3), (self.height /3 )]
                elif self.subnumber == 1 or  self.subnumber == 3:
                    self.rect2[0] = [self.x , self.y + (self.height/3), (self.width/3), (self.height*2/3)]
                    self.rect2[1] = [self.x +(self.width/3)  , self.y +(self.height/3), (self.width/3), (self.height/3)]
                    self.rect2[2] = [self.x +((self.width/3)*2)  , self.y , (self.width/3), (self.height*2/3 )]
        
                pygame.draw.rect(win, (255,0,0), (self.rect2[0]) ,2)
                pygame.draw.rect(win, (255,0,0), (self.rect2[1]) ,2)
                pygame.draw.rect(win, (255,0,0), (self.rect2[2]) ,2)