import pygame
class HeroPlane(object):
    def __init__(self,img_path,screen):
        self.screen=screen
        self.x=(400-100)/2
        self.y=350
        self.w=100
        self.h=124
        self.img_path=img_path
        self.hero_plane=pygame.image.load(self.img_path)
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
        self.bullet_list=[]

    def display(self):
        self.screen.blit(self.hero_plane,self.rect)
        for i in self.bullet_list:
            i.display()
            i.move()
    def fire(self):
        self.bullet_list.append(Bullet('./images/bullet.png',self.screen,self.rect.x,self.rect.y))
    def fire2(self):
        self.bullet_list.append(Bullet('./images/bullet.png',self.screen,self.rect.x+80,self.rect.y))


class Bullet(object):
    def __init__(self,img_path,screen,x,y):
        self.screen=screen
        self.x=x
        self.y=y
        self.img_path=img_path
        self.bullet=pygame.image.load(self.img_path)
    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y))
    def move(self):
        self.y -=2
def Key_control(hero,move_step):

    #游戏事件的监听  控制
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#退出游戏
            print('游戏退出')
            pygame.quit()
            exit() #退出程序
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hero.fire()
                hero.fire2()

        '''
        elif event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_UP:
                rect.y -=move_step
            elif event.key ==pygame.K_DOWN:
                rect.y +=move_step
            elif event.key ==pygame.K_LEFT:
                rect.x -= move_step
            elif event.key ==pygame.K_RIGHT:
                rect.x +=move_step
        elif event.type == pygame.KEYUP:
            pass

        '''


    keys_pressed =pygame.key.get_pressed()
    if keys_pressed[pygame.K_SPACE]:
        hero.fire()
        hero.fire2()
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        hero.rect.x+=move_step
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        hero.rect.x-=move_step
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        hero.rect.y-=move_step
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        hero.rect.y+=move_step



def main():
    screen = pygame.display.set_mode((400,500),0,32)
    background=pygame.image.load('./images/background.png')
    # 定义好的位置，和尺寸

    hero=HeroPlane('./images/hero1.png',screen)
    clock=pygame.time.Clock()#获得游戏时钟 控制器
    move_step=10#移动的步长值

    while True:
        screen.blit(background,(0,0))
        hero.display()
        Key_control(hero,move_step)
                #刷新显示
        pygame.display.update()
        clock.tick(60)#让游戏时钟，1/60秒运行一次


if __name__=='__main__':
    main()
