class xrk:
    def __init__(self,name,yanse,jin):
        xrk.name = name
        xrk.yanse = yanse
        xrk.jin=jin
    def guang1(self):
        print('种植了一棵%s' %(self.name))
    def guang2(self):
        print('%s放出了%s阳光' %(self.name,self.yanse))
    def guang3(self):
        print('%s在疯狂的生产%s'%(self.name,self.jin))
    def __str__(self):
        a='名字是 :'+self.name +'颜色是 ：'+self.yanse+'金币是 :'+self.jin
        return a
xiangrikui=xrk('向日葵','黄色','50$')
print(xiangrikui)
print(id(xiangrikui))
xiangrikui.guang1()
xiangrikui.guang2()
xiangrikui.guang3()
class Wd:
    def __init__(self,name,yanse,faxing):
        Wd.name=name
        Wd.yanse=yanse
        Wd.faxing=faxing
    def Wd(self):
        print('种植了一棵%s' %(self.name))
    def Wd1(self):
        print('%s的颜色是%s'% (self.name,self.yanse))
    def Wd2(self):
        print('%s的发型是%s'%(self.name,self.faxing))
    def Wd3(self):
        print('%s在疯狂的摇头' %(self.name))
    def Wd4(self):
        print('%s射出了很多%s的子弹'% (self.name,self.yanse))
    def Wd5(self):
        print('%s一晃一晃的突突突'% (self.name))
        print('%s的子弹射到了僵尸的身上看着好疼'%(self.name))
    def __str__(self):
        b='名字是 :'+self.name +'颜色是 :'+self.yanse + '发型是 :'+self.faxing
        return b
Wd=Wd('豌豆','绿色','三毛')
print(Wd)
print(id(Wd))
Wd.Wd()
Wd.Wd1()
Wd.Wd2()
Wd.Wd3()
Wd.Wd4()
Wd.Wd5()
class Jg:
    def __init__(self,name,yanse):
        Jg.name=name
        Jg.yanse=yanse
    def Jg(self):
        print('种植了一个%s'% (self.name))
    def Jg1(self):
        print('坚果颜色是%s'%(self.yanse))
    def Jg2(self):
        print('%s被僵尸咬了一口'%(self.name))
    def Jg3 (self):
        print('%s跳了起来了阻挡了僵尸的脚步'% (self.name))
    def Jg4(self):
        print('%s被僵尸咬的遍体鳞伤'%(self.name))
    def __str__(self):
        a='名字是 :'+self.name +'颜色是 :'+ self.yanse
        return a
Jg=Jg('坚果','土黄色')
print(Jg)
print(id(Jg))
Jg.Jg()
Jg.Jg1()
Jg.Jg2()
Jg.Jg3()
Jg.Jg4()
class Js:
    def __init__(self,name,yanse,xieliang):
        Js.name=name
        Js.yanse=yanse
        Js.xieliang=xieliang
    def Js(self):
        print('%s的%s向房子跑去 '%(self.yanse,self.name))
    def Js1(self):
        print('%s在咬坚果'%(self.name))
    def Js2 (self):
        print('%s跳了起来 跳向了房子'%(self.name))
    def Js3 (self):
        print('有一个%s死了'% (self.name))
    def Js4(self):
        print('有更多的%s死下了'% (self.name))
    def Js5(self):
        print('又出来一波%s每个%s的血量都是%s'%(self.name,self.name,self.xieliang))
    def __str__(self):
        a="名字是 :"+self.name +'颜色是 :'+self.yanse+'血量是 :'+self.xieliang
        return a
Js=Js('僵尸','石灰色','100点')
print(Js)
print(id(Js))
Js.Js()
Js.Js1()
Js.Js2()
Js.Js3()
Js.Js4()
Js.Js5()
