class Test(object):
    def __init__(self):
        self.switch='open'
    def div(self,a,b):
        try:
            return a/b
        except Exception as ret:
            if self.switch=='open':
                print('出现异常：%s'%ret)
            else:
                raise
t=Test()
#控制开关  open打开状态不抓取异常 close关闭抓取异常
#t.seitch='close'

print(t.div(2,0))#修改参数控制

