while True:
    import random
    a = random.randint (1,6)
    b = random.randint (1,6)
    c = random.randint (1,6)
    d = a+b+c
    print ('*'*50)
    e=int(input('你要输入的点数是'))
    while e>18:
        e=int(input('你需要在输入一次'))
    if e<10:
        print ('您买的是小')
    else:
        print ('您买的是大')
    print ('第一次的点数是 %d ,第二次的点数是 %d ,第三次的点数是 %d ,最后一次 的点数是 %d' % (a,b,c,d))
    if d<=9:
        print ('电脑小')
    else:
        print ('电脑大')
    if e<=9 and d<=9 or e>9 and d>9:
        print ('你赢了恭喜你')
    else:
        print ('你输了不好意思')
