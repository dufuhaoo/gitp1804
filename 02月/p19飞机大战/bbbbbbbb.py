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
        self.x=x
        self.y=y
        self.yx=pygame.image.load(self.lujing)

    def display(self):
        self.screen.blit(self.yx,(self.x,self.y))
    def move(self):
        self.y -= 5


def main():
    screen=pygame.display.set_mode((400,500),0,0)
    bj=pygame.image.load('./images/background.png')
    yx=FeiJi('./images/hero1.png',screen)


    rect=pygame.Rect((400-100)/2,350,100,124)
    move_step=5
    while True:
        screen.blit(bj,(0,0))
        yx.display()

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                exit()



        keys_pressed =pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            yx.fire()
        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            yx.rect.x+=move_step
        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            yx.rect.x-=move_step
        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            yx.rect.y-=move_step
        if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            yx.rect.y+=move_step

        pygame.display.update()
main()

