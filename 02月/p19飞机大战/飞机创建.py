import time
import pygame
def main():

    screen = pygame.display.set_mode((400,500),0,32)
    background=pygame.image.load('./images/background.png')
    aa=pygame.image.load('./images/enemy1.png')
    hero_play=pygame.image.load('./images/hero1.png')
    # 定义好的位置，和尺寸
    rect =pygame.Rect((400-100)/2,350, 100,124)
    bb=pygame.Rect(200,50 , 100,124)
    clock=pygame.time.Clock()#获得游戏时钟 控制器
    while True:
        screen.blit(background,(0,0))
        screen.blit(aa,bb)

        screen.blit(hero_play,rect) #设置飞机

        rect.x += 1#移动
        if rect.x >400:
            rect.x =0

        bb.x += 1#移动
        if bb.x > 400:
            bb.x = 0
        for event in pygame.event.get():
            print('event.type=',event,type)
            print('event=',event)
            if event.type==pygame.QUIT:
                print('游戏退出')
                pygame.quit()
                exit()#退出程序

        #刷新显示
        pygame.display.update()
        clock.tick(60)#让游戏时钟，1/60秒运行一次


'''
feiji =pygame.Rect(100,500,50,50)
print('x=',feiji.x)
print('y=',feiji.y)
print('width=',feiji.width)
print('height=',feiji.height)
'''


if __name__=='__main__':
    main()
