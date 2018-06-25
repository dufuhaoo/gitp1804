
import pygame

class FuLei(object):
    def __init__(self,img_path,screen,x,y):#初始化 游戏框架 飞机图片
        self.screen=screen #游戏框架
        self.x=x#飞机坐标x轴
        self.y=y#飞机坐标y轴
        self.w=100#飞机宽度
        self.h=124#飞机长度
        self.img_path=img_path#初始化飞机图片
        self.plane=pygame.image.load(self.img_path)#飞机图片
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)#定义飞机尺寸
        self.bullet_list=[]#定义列表装子弹
    def display(self):
        self.screen.blit(self.plane,self.rect)
        for i in self.bullet_list:#循环输出子弹
            if i.judge():
                self.bullet_list.remove(i)
            i.display()#子弹的对象.disply跟着飞机走
            i.move()#子弹


