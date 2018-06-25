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
    def display(self):
        self.screen.blit(self.yx,self.rect)
        if self.rect.x>300:
            self.rect.x=300
        elif self.rect.x<=0:
            self.rect.x=0
        if self.rect.y>400:
            self.rect.y=400
        elif self.rect.y<=0:
            self.rect.y=0
def main():
    screen=pygame.display.set_mode((400,500),0,0)
    bj=pygame.image.load('./images/background.png')
    yx=FeiJi('./images/hero1.png',screen)
    move_step=5
    while True:
        screen.blit(bj,(0,0))
        yx.display()
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
                exit()
        aa=pygame.key.get_pressed()
        if aa[pygame.K_RIGHT] or aa[pygame.K_d]:
            yx.rect.x += move_step
        if aa[pygame.K_LEFT] or aa[pygame.K_a]:
            yx.rect.x -= move_step
        if aa[pygame.K_UP] or aa[pygame.K_w]:
            yx.rect.y -= move_step
        if aa[pygame.K_DOWN] or aa[pygame.K_s]:
            yx.rect.y += move_step

        pygame.display.update()
main()
