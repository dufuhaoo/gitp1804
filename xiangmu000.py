'''

思路：淘宝网店  1,网页提示有什么样的商品
2, 选择有什么样的商品
3，产看购买过商品人的评论
4,查看型号
5，联系客服询问发什么样的快递
6,选择地址填写信息
7,点击付款
选择付款方式   （微信支付 ，支付宝，银行卡）
输入密码付款
'''
list_aa=[]#定义一个列表来装物品
dic_dian={}
dic_aa={}
def pc():
    print('*='*10)
    print('------欢迎来到淘宝---- *')
    print('1, 搜索商品         *')
    print('2, 客服问答         *')
    print('3, 查看购物车并购买 *')
    print('4, 查看快递         *')
    print('5, 查看评论         *')
    print('6, 退款             *')
    print('7, 购买别的货物     *')
    print('8,退出               ')
    print('*='*10)
pc()
def sousuo():
    print('我们这里都有：')
    print('          外套      *')
    print('>.< '*2)
    print('          裤子      *')
    print('>.< '*2)
    print('          鞋子      *')
    print('>.< '*2)
    print('          零食      *')
    print('>.< '*2)
def wenda():
    while True:
        print('*'*10)
        aa=input('亲 ：请问您有什么需要？\n1衣服质量 \n2衣服大小 \n3衣服价格 \n4衣服款式 \n如果问完了请输入q')
        if aa=='q':
            break
        elif aa=='1':
            print('——————————————————————————————————————————————')
            print('亲 衣服质量可以放心绝对让您放心')
        elif aa=='2':
            print('——————————————————————————————————————————————')
            print('亲:M号 衣长65 肩宽60 袖长56 L号 衣长67 肩宽60 袖长56 LX号 衣长69 肩宽64 袖长56 您可以参考一下')
        elif aa=='3':
            print('——————————————————————————————————————————————')
            print('亲：衣服价格绝对是全网最低的  绝对让您无忧所值')
        elif aa=='4':
            print('——————————————————————————————————————————————')
            print('亲：衣服款式是韩版时尚气质防晒衫')
        else:
            print('——————————————————————————————————————————————')
            print('亲：请稍后等待客服小姐姐暂时不在线')
        print('*'*10)



def diao():
    aa=input('请输入您的微信6位支付密码')
    if len(aa) ==6:#如果从屏幕上获取的不是6位必须在次输入
        print('您已支付成功我们会尽快给您安排发货')
    else:
        while len(aa) !=6:
            aa=input('您输入的密码有误请重新输入')



def fuzhang():
    zhifu=input('请选择你的支付方式 1微信 2支付宝 3银行卡')
    if zhifu=='1':
        diao()
    elif zhifu=='2':
        diao()

    else:
        diao()
bob=0

def chaKan():

    xuanZe=input('我们这里有 \n1:外套\n 2:鞋子\n 3:裤子\n 4:零食\n 请问你要购买:   ')
    if xuanZe=='1':
        mai=input('阿迪达斯外套价格360元请问是否要购买 请选1')
        print('   ')
        print( '     **** ****')
        print( '    * *  *  * *')
        print( '   * *   *   * *')
        print( '  * *    *    * *')
        print( ' *  ***********  *')
        print('    ')
        dic_dian['外套']='阿迪达斯'
        if mai=='1':#这里是选择支付方式和支付的方式
            fuzhang()#调用上面的付账方式
    elif xuanZe=='2':
        naike=input('耐克牌北京老布鞋价格240元请问是否购买请选1 不买选2 ')
        print('耐克牌北京老布鞋')
        print('    **      **')
        print('   *==*    *==*')
        print('   *==*    *==*')
        print('   *__*    *__*')
        print('   ****    ****')
        print('  ')
        dic_dian['鞋子']='耐克'#同上面一样
        if naike=='1':
            fuzhang()
    elif xuanZe=='3':#同上面一样
        bb=input('我的同款裤子150元请问是否购买 请选1不买 2')
        print('  *********' )
        print('  *___*___* ')
        print('  *///*///* ')
        print('  *  * *  * ')
        print('  *  * *  * ')
        print('  *  * *  * ')
        print(' *   * *   * ')
        dic_dian['裤子']='喇叭裤'
        if bb=='1':
           fuzhang()
    else:#同上面一样
        songshu=input('三只松鼠零食大礼包200元请问您是否购买 请选1不买选2')
        dic_dian['零食']='三只松鼠'
        if songshu=='1':
           fuzhang()

def kuaidi():
    user=input('请选择是否要查看您的快递 是1  不是2')
    if user=='1':
        if len(dic_dian) ==1:
            print('您的快递已发送单号是2245 请注意查收',dic_dian)
        else:
            print('对不起您没有购买商品请你购买后再来查询')
    else:
        print('好的祝您使用愉快')
def pinglun():
    print('—+——+——+——+——+——+——+——+——+——+——+——+——+——++——+——+——+——+——+')
    print('大花：商品很不错啊好评好评商家服务态度也很好  快递很快就到了 感觉很适合我')
    print('小明：哇真是良心商家啊感觉 自己遇到了知己  哈哈哈！！！')
    print('大头：这家店真的很好啊 不错下次还来，期待下次合作')
    print('小头：感觉还不错把值得信赖')
    print('丫丫：恩  我就是为了好评红包  就当我路过')
    print('——+——+——+——+——+——+——+——+——+——+——+——+——+——+——+——+——+——+——+—')
    a=input('你可以进行评论：')
    print('  ')
    print('++++++++++++')
    print('  ')
    print('我的评论',a)
    print('   ')
    print('++++++++++++')
    print('   ')
def tuikuan():
    print('#####################')
    print('正在为您退款     ')
    print('您的订单正在运作中请耐心等待')
    print('                      ')
    print('#####################')
def zeng():
    tianjia=input('请问你是否还有想买的商品我们安排为您进货1是 2不是')
    if tianjia=='1':
        bb=input('输入你要买的商品名称')
        list_aa.append(bb)
        print(list_aa)
    if tianjia=='3':
        cd=int(input('请问你要改第几个商品'))
        dc=input('输入改为什么：')
        list_aa[cd-1]=dc
        print(list_aa)
    elif tianjia=='2':
        print('很遗憾！！')

while True:#整个大循环
    aa=input('请输入你要选择的功能')
    if aa=='1':
        sousuo()
    elif aa=='2':
        wenda()
    elif aa=='3':
        chaKan()
        print('你买的东西是：',dic_dian)
    elif aa=='4':
        kuaidi()
    elif aa=='5':
        pinglun()
    elif aa=='6':
        tuikuan()
    elif aa=='7':
        zeng()
        print(dic_aa)
    else:#调用上面的8号功能实现退出
        break
