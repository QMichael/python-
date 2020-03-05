#读取文本
f=open('D:/qw/english.txt','r')
a=[]
#丢掉段落后的换行符，并返回列表
for s in f.readlines():
    a.extend(s.replace('\n','').split(' '))
#对列表去重
a=list(set(a))
#对列表排序
a.sort()
#写入文本
f2=open('D:/qw/english2.txt','w')
f2.write('\n'.join(a))
#文本关闭
f.close()
f2.close()
