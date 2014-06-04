#__author__ = 'SinnerA'
#coding=utf-8
import urllib2
import re
import thread
import time

class HTMLModel:
    def __init__(self):
        self.pageCount = 1
        self.pages = []
        self.enable = False

    #得到当前页面信息
    def getPage(self, pageCount):
        #伪装成浏览器访问
        reqHead = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        url = "http://m.qiushibaike.com/hot/page/" + pageCount
        request = urllib2.Request(url, reqHead)
        response = urllib2.urlopen(request)
        #页面转成utf-8编码
        pageInfo = response.decode("utf-8")
        myItems = []
        items = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>', pageInfo, re.S)
        for item in items:
            myItems.append([item[0].replace("\n", ""), item[1].replace("\n", "")])
        return myItems

    def loadPage(self):
        #用户未输入quit
        while self.enable:
            if len(self.pages) < 2:
                try:
                    #获取新的页
                    myPage = self.getPage(str(self.pageCount))
                    self.page += 1
                    self.pages.append(myPage)
                except Exception,e:
                    print "无法连接糗事百科！"
                    print e
            else:
                time.sleep(1)

    def showPage(self, items, pageCount):
        for item in items:
            print "第%d页" % pageCount, item[0]
            print item[1]
            myInput = raw_input()
            if myInput == "quit":
                self.enable = False
                break

    def start(self):
        self.enable = True
        pageCount = self.pageCount

        thread.start_new_thread(self.loadPage(), ())

        while self.enable:
            items = self.getPage(pageCount)
            self.showPage(items, pageCount)
            del self.pages[0]
            pageCount += 1

raw_input(" ")
myModel = HTMLModel()
myModel.start()




