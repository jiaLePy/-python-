#encoding=utf-8
import wenjian
t=wenjian.xinxi()
for i in t:
    l=eval(i)
    ll=l[0]
    #ll.decode("ascii").encod("utf-8")
    print('=============name=============')
    print (ll)
    print('\n')
    print('------------salary------------')   
    print(l[1])
    print('\n')
    print('------------addr--------------')
    for xx in l[2]:
        print(xx,end='')
    print('\n')
    print('------------content-----------')
    for xxx in l[3]:
        print(xxx)
