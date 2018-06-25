from jichu import *
import pygame#插入pygame包
import random
class DiJi(FuLei):#定义飞机类
    def __init__(self,img_path,screen):#初始化 游戏框架 飞机图片
        FuLei.__init__(self,img_path,screen,0,0)
        self.flag='right'
    def move(self):#定义move方法控制敌机移动
        if self.flag =='right':
            self.rect.x += 2
        else:
            self.rect.x -=2
        if self.rect.x >440 -self.rect.width:
            self.flag ='left'
        elif self.rect.x<=0:
            self.flag ='right'
    def fire(self):#开火方法
        self.bullet_list.append(DiJiBullet('./images/bullet1.png',self.screen,self.rect.x,self.rect.y))

class DiJiBullet(object):#创建Bullet子弹类
    def __init__(self,img_path,screen,x,y):#初始化子弹图片游戏框架 x，y
        self.screen=screen #初始化游戏框架
        self.x=x+40
        self.y=y+20
        self.img_path=img_path#初始化子弹图片
        self.bullet=pygame.image.load(self.img_path)#子弹图片
    def display(self):#把子弹装如框架并使用飞机的xy轴跟随飞机动
        self.screen.blit(self.bullet,(self.x,self.y))

    def move(self):#定义子弹的步长
        self.y +=2
    def judge(self):#判断子弹是否飞出屏幕外
        if self.y>500:
            return True#表示飞出屏幕

        else:
            return False#没有飞出屏幕





class HeroPlane(FuLei):#定义飞机类
    def __init__(self,img_path,screen):#初始化 游戏框架 飞机图片
        FuLei.__init__(self,img_path,screen,(400-100)/2,350)
        '''
    def display(self):#把飞机装入游戏框架中
        self.screen.blit(self.plane,self.rect)
        for i in self.bullet_list:#循环输出子弹
            if i.judge():
                self.bullet_list.remove(i)
            i.display()#子弹的对象.disply跟着飞机走
            i.move()#子弹对象调用move方法依次走2步
        '''
    def fire(self):#开火方法
        self.bullet_list.append(Bullet('./images/bullet.png',self.screen,self.rect.x,self.rect.y))

class Bullet(object):#创建Bullet子弹类
    def __init__(self,img_path,screen,x,y):#初始化子弹图片游戏框架 x，y
        self.screen=screen #初始化游戏框架
        self.x=x+40
        self.y=y+20
        self.img_path=img_path#初始化子弹图片
        self.bullet=pygame.image.load(self.img_path)#子弹图片
    def display(self):#把子弹装如框架并使用飞机的xy轴跟随飞机动
        self.screen.blit(self.bullet,(self.x,self.y))
    def move(self):#定义子弹的步长
        self.y -=2
    def judge(self):#判断子弹是否飞出屏幕外
        if self.y<0:
            return True#表示飞出屏幕

        else:
            return False#没有飞出屏幕

def Key_control(hero,move_step):

    #游戏事件的监听  控制
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#退出游戏
            print('游戏退出')
            pygame.quit()
            exit() #退出程序
        elif event.type ==pygame.KEYDOWN:#定义如果点击空格K_SPACE发射子弹
            if event.key == pygame.K_SPACE:
                hero.fire()#调用发射fire功能

                #监听控制上下左右键  或者w a s d键
    keys_pressed =pygame.key.get_pressed()
    if keys_pressed[pygame.K_SPACE]: #这一步控制长按空格键一直发火
        hero.fire()
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        if hero.rect.x < 400 - hero.rect.width:
            hero.rect.x+=move_step
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        if hero.rect.x >=0:
            hero.rect.x-=move_step
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        if hero.rect.y >=0:
            hero.rect.y-=move_step
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        if hero.rect.y <500-hero.rect.height:
            hero.rect.y+=move_step



def main():
    screen = pygame.display.set_mode((400,500),0,32)#设置游戏框架
    background=pygame.image.load('./images/background.png')
    # 定义好的位置，和尺寸

    hero=HeroPlane('./images/hero1.png',screen)
    diji=DiJi('./images/enemy1.png',screen)
    #创建对象传入子弹图片和游戏框架
    clock=pygame.time.Clock()#获得游戏时钟 控制器
    move_step=10#移动的步长值

    while True:
        Key_control(hero,move_step)
        screen.blit(background,(0,0))#设置游戏背景大小
        hero.display()#调用display把飞机装如框架
        diji.display()

        diji.move()#调用move方法实现敌机移动
        aa=random.randint(1,60)
        if aa==30:
            diji.fire()

        pygame.display.update()
        clock.tick(60)#让游戏时钟，1/60秒运行一次


if __name__=='__main__':
    main()
