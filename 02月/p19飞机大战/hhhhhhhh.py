import pygame
class FeiJi(object):
    def __init__(self,lujing,screen):
        self.screen=screen
        self.lujing=lujing
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
            i.display()
            i.move()
    def fire(self):
        zd=ZiDan('./images/bullet.png',self.screen,self.rect.x,self.rect.y)
        self.aa_list.append(zd)

class ZiDan(object):
    def __init__(self,lujing,screen,x,y):
        self.screen=screen
        self.lujing=lujing
        self.x=x+40
        self.y=y+20
        self.yx=pygame.image.load(self.lujing)
    def display(self):
        self.screen.blit(self.yx,(self.x,self.y))
    def move(self):
        self.y -=5


def main():
    screen=pygame.display.set_mode((400,500),0,32)
    bj=pygame.image.load('./images/background.png')
    yx=FeiJi('images/hero1.png',screen)
    move=5
    while True:
        screen.blit(bj,(0,0))
        yx.display()
        pygame.display.update()

        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
                exit()
        aa=pygame.key.get_pressed()
        if aa[pygame.K_SPACE]:
            yx.fire()
        if aa[pygame.K_RIGHT]:
            if yx.rect.x<400-100:
                yx.rect.x +=move
        if aa[pygame.K_LEFT]:
            if yx.rect.x >0:
                yx.rect.x -=move
        if aa[pygame.K_UP]:
            if yx.rect.y >0:
                yx.rect.y -=move
        if aa[pygame.K_DOWN]:
            if yx.rect.y<500-124:
                yx.rect.y +=move

if __name__=='__main__':
    main()
