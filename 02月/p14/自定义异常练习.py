class MyError(Exception):
    def __init__(self,str_error):
        self.name=str_error


def denglu():
    zh=int(input('账户'))
    if zh !=123456789:
        raise MyError('账户格式错误')
def mima():
    mi=input('密码')
    if len(mi)<6:
        raise MyError('密码小于6位')
try:
    denglu()
    mima()
except Exception as re:
    print('遇到了异常：内容是%s'%re)

