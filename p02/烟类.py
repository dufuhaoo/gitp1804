class yan():
    def mai1(slef):
        print('唉来了卖烟了上好的烟%s' % (slef.name))
    def mai2(slef):
        print('买一盒买一盒')
    def xi(slef):
        print('抽一根？')
    def jieshao(self):
        print('烟名是%s 价格是%d 颜色是%s' % (self.name,self.price,self.color))
dihaoyan = yan()
dihaoyan.price=10
dihaoyan.color='黄色'
dihaoyan.name='   帝豪烟'
dihaoyan.jieshao()
dihaoyan.mai1()

zhonghua=yan()
zhonghua.price=60
zhonghua.color='红色'
zhonghua.name='   中华烟'
zhonghua.jieshao()
zhonghua.mai1()


huanghe = yan()
huanghe.price=25
huanghe.color='黄色'
huanghe.name='  黄鹤楼'
huanghe.jieshao()
huanghe.mai1()
