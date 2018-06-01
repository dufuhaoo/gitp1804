f=open('ts.txt','w')
f.write('窗前明月光\n意识地上双\n举头往明月\n低头思故乡\n')
f.close()

f=open('ts.txt','r')
a=f.readlines()
f.close()

f=open('ts.txt','w')
for i in a:
    xx=print(i[0:-1]+'**')
f.close()
print('文件名是%s' % f.name)
print('文件是否关闭%s' % f.closed)
print('文件是以模式打开%s' % f.mode)
f.close()
