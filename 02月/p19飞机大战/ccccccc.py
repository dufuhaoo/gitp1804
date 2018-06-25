import pygame
class FeiJi(object):
    def __init__(self,lujing,screen):
        self.lujing=lujing
        self.screen=screen
        self.x=(400-100)/2
        self.y=350
        self.w=100
        self.h=124
        self.yx=pygame.image.load(self.lujing)
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
        self.aa_list=[]
    def display(self):
        self.screen.blit(self.yx,self.rect)
        for i in self.aa_list:
            i.adisplay()
            i.move()

        if self.rect.x>300:
            self.rect.x=300
        elif self.rect.x<=0:
            self.rect.x=0
        if self.rect.y>400:
            self.rect.y=400
        elif self.rect.y<=0:
            self.rect.y=0
    def fire(self):
        zd=ZiDan('./images/bullet.png',self.screen,self.rect.x,self.rect.y)

        self.aa_list.append(zd)
class ZiDan(object):
    def __init__(self,lujing,screen,x,y):
        self.x=x
        self.y=y
        self.lujing=lujing
        self.screen=screen
        self.zd=pygame.image.load(self.lujing)
    def adisplay(self):
        self.screen.blit(self.zd,(self.x,self.y))

    def move(self):
        self.y -= 5



def main():
    screen=pygame.display.set_mode((400,500),0,0)
    bj=pygame.image.load('./images/background.png')
    yx=FeiJi('./images/hero1.png',screen)

    while True:
        jianting(yx,5)
        screen.blit(bj,(0,0))
        yx.display()
        pygame.display.update()

def jianting(yx,move):
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            exit()
        elif i.type==pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                yx.fire()

    aa=pygame.key.get_pressed()
    if aa[pygame.K_RIGHT] or aa[pygame.K_d]:
        yx.rect.x += move
    if aa[pygame.K_LEFT] or aa[pygame.K_a]:
        yx.rect.x -= move
    if aa[pygame.K_UP] or aa[pygame.K_w]:
        yx.rect.y -= move
    if aa[pygame.K_DOWN] or aa[pygame.K_s]:
        yx.rect.y += move
if __name__=='__main__':
    main()
