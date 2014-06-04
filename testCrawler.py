#coding=utf-8
import string,urllib2

def baidu_tieba(url, begin_page, end_page):
    for i in range(begin_page,end_page+1):
        pageName = string.zfill(i, 5) + ".html"
        print "正在下载第" + str(i) + "页，保存为" + pageName + "......"
        f = file(pageName, "w+")
        page = urllib2.urlopen(url+str(i)).read()
        f.write(page)
        f.close()
#调用
url=str(raw_input("输入贴吧地址："))
begin_page = int(raw_input("开始页："))
end_page = int(raw_input("结束页："))

baidu_tieba(url,begin_page, end_page)
