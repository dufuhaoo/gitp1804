class Calc(object):
    aa=None
    bb=False
    def __init__(self,name):
        if Calc.bb==False:
            self.name=name
            Calc.bb=True
    def __new__(cls,*k):
        if cls.aa==None:
            cls.aa =object.__new__(cls)
            return cls.aa
    def jia(self,a,b):
        return a+b
    def jian(self,a,b):
        return a-b
    def chu(self,a,b):
        return a/b
    def cheng(self,a,b):
        return a*b
class YunSuan(Calc):
    def jisuan(self,x,fuhao,y):
        if fuhao=='+':
            aa= super().jia(x,y)
        elif fuaho=='-':
            aa= super().jian(x,y)
        elif fuhao=='/':
            aa= super().chu(x,y)
        elif fuaho=='*':
            aa= super().cheng(x,y)
        else:
            print('计算有误')
        print(aa)
aa=input('输入一个计算机名')
c1=YunSuan(aa)
while True:
    a=int(input('请输入第一个数字'))
    b=input('请输入运算符号')
    c=int(input('请输入第二个数字'))
    c1.jisuan(a,b,c)
