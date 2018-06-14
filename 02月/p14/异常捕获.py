'''
try:
    print(1)
    open('a.txt','r')
    print(asdasdas)
except (NameError):
    print('程序异常')
'''
try:
    a=input('输入一个文件名称')
    f.open(a,'w')
    f.close()
    f.open(a,'r')
    ren=f.read()
    print(ren)
    f.close()
except (TypeError,NameError):
    print('程序出问题了')
