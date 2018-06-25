import pygame
class FeiJi(object):
    def __init__(self,dizhi,chuangko):
        self.chuangko=chuangko
        self.x=(400-100)/2
        self.y=350
        self.w=100
        self.h=124
        self.dizhi=dizhi
        self.feitu=pygame.image.load(self.dizhi)
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
        self.bullet_list=[]
    def display(self):
        self.chuangko.blit(self.feitu,self.rect)
        for i in self.bullet_list:
            i.display()
            i.move()
    def fire(self):
        self.bullet_list.append(Bullet('./images/bullet.png',self.chuangko,self.rect.x,self.rect.y))
class Bullet(object):
    def __init__(self,dizhi,chuangko,x,y):
        self.chuangko=chuangko
        self.x=x
        self.y=y
        self.dizhi=dizhi
        self.bullet =pygame.image.load(self.dizhi)
    def display(self):
        self.chuangko.blit(self.bullet,(self.x,self.y))
    def move(self):
        self.y -=2
def Key_control(hero,move_step):
    for i in pygame.event.get():
        if i.type ==pygame.QUIT:
            print('退出游戏')
            pygame.quit()
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                    hero.fire()
        elif i.type == pygame.KEYUP:
            pass
    aa=pygame.key.get_pressed()
    if aa[pygame.K_SPACE]:
        hero.fire()
    if aa[pygame.K_RIGHT] or aa[pygame.K_d]:
        hero.rect.x +=move_step
    if aa[pygame.K_LEFT] or aa[pygame.K_a]:
        hero.rect.x -= move_step
    if aa[pygame.K_UP] or aa[pygame.K_w]:
        hero.rect.y -= move_step
    if aa[pygame.K_DOWN] or aa[pygame.K_s]:
        hero.rect.y+= move_step
def main():
    chuangko =pygame.display.set_mode((400,500),0,32)

    background =pygame.image.load('./images/background.png')

    hero = FeiJi('./images/hero1.png',chuangko)
    while True:
        chuangko.blit(background,(0,0))
        hero.display()
        Key_control(hero,10)
        pygame.display.update()
if __name__ =='__main__':
    main()

