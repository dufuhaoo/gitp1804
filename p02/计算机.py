try:
    class JS(object):
        __aa=None
        __bb=False
        def __init__(self,name):
            if self.__bb==False:
                self.name=name
                self.__bb=True

        def jia(self,a,b):
            return a+b
        def jian(self,a,b):
            return a-b
        def cheng(self,a,b):
            return a*b
        def chu(self,a,b):
            return a/b
        def jisuan(self):
            aa=int(input('请输入第一个数字'))
            while True:
                bb=input('请输入你的运算操作付')
                if bb =='=':
                    break
                cc=int(input('请输入第三个数字是:'))
                if bb =='+':
                    aa=self.jia(aa,cc)
                elif bb =='-':
                    aa=self.jian(aa,cc)
                elif bb =='*':
                    aa=self.cheng(aa,cc)
                elif bb =='/':
                    aa=self.chu(aa,cc)
                print(aa)
            print(aa)
        def __new__(cls,*k):
            if cls.__aa==None:
                cls.__aa=super().__new__(cls)
            return cls.__aa
    name=input('请创建一个计算机')

    js=JS(name)
    print(js.name)
    js.jisuan()
except Exception as a:
    print('程序报错了%s'% a)
else:
    print('程序没问题')


