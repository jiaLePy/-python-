#encoding=utf-8
import time
import urllib
import urllib2
import liebiao
from bs4 import BeautifulSoup
def shuaixuan(temp):
    a=int(temp.find("www"))
    b=int(temp.find(".html"))
    x=temp[a:b+5]
    return x
'''
x=1
newlie=[]
while x<21:
    url='http://www.lagou.com/zhaopin/Python/'+str(x)
    response=urllib2.urlopen(url)
    soup=BeautifulSoup(response.read())
    #print (soup.prettify())
    #print soup.select('a[class="position_link"]')
    liebiao=soup.select('a[class="position_link"]')
    for l in liebiao:
        m=str(l)
        newlie.append(shuaixuan(m))
    time.sleep(2)
    x+=1
print(newlie)
#获取300条职位链接，放在newfile
'''

def gongsi(temp):
    dd=[]
    response=urllib2.urlopen(temp)
    soup=BeautifulSoup(response.read())
    a=soup.select('h1 > div')
    t=a[0].string # 公司名称
    dd.append(t)
    
    b=soup.select('dd[class="job_request"]')
    c=b[0]
    d=c.select('span[class="red"]')
    e=d[0].string    #薪资
    dd.append(e)
    
    f=soup.select('div[class="work_addr"]')
    z=' '
    gg=f[0]
    ggg=gg.select('a')
    di=[]
    for i in ggg:
        k=i.string
        di.append(k)
    
    dd.append(di)   #地址
    
    ww=[]
    y=soup.select('dd[class="job_bt"]')
    yy=y[0]
    yyy=yy.select('p')
    for m in yyy:
        m1=m.string
        ww.append(m1)
    dd.append(ww)    #职位信息
    return dd    


i=0
l=liebiao.aa()
ak=[]
while i<100:
    l1='http://'+l[i]
    
    d6=str(gongsi(l1))
    ak.append(d6)
    i+=1
    time.sleep(2)


q=open('wenjian.py','w')
q.write(str(ak))
q.close()


