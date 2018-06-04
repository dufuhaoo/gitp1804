def name(name):
    f=open(name,'r')
    p = name.rfind('.')
    a1 = name[:p]
    a2 = name[p:]
    b=open(a1+'-副本'+a2 ,'w')
    while True:
        a=f.read(1024)
        if len(a)==0:
            break
        b.write(a)
    f.close()
    b.close()

a=input('输入你想要复制的文件名')
name(a)
