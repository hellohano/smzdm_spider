# coding:utf-8
__author__ = 'hano'
import urllib2
import re
import BeautifulSoup as bs


def main():
    getWebContent("http://bt.ktxp.com/today.html#1")
    # print getWebContent("http://www.baidu.com")


def getWebContent(url):
    if (url == None):
        return "the url is null !"
    else:
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req)
        webContent = resp.read()
        soup = bs.BeautifulSoup(webContent)

        divs = soup.findAll('div', attrs={'class': 'item-box round-corner space-bottom'})

        for div in divs:
            # this div contains the section title(like music/game ..) and the list of resource
            open('ktxp.txt', 'a').write("========= section " + div.find('h2').contents[0].string.encode('utf-8') + " begin =========\n")
            tbody = div.find('table').find('tbody')
            resList = tbody.findAll('tr')
            for item in resList:
                analystKTXPItem(item)
            open('ktxp.txt', 'a').write("========= section end =========\n\n")
        return divs


def analystKTXPItem(item):
    # ================== the ktxp res item strut ============================
    # date|resource title    |resource size|seed nums      |download nums  |publisher
    # td  |td(ltext ttitle)/a|      td     |td(class/bts-2)|td(class/btl-1)|td/a(class/team-name)
    # ================== end ================================================
    nodes = item.findAll('td')
    date = nodes[0].string
    title = item.find('td', attrs={'class': 'ltext ttitle'}).contents[1].string
    size = nodes[2].string
    seedNum = item.find('td', attrs={'class': re.compile('^bts')}).string
    DownloadNum = item.find('td', attrs={'class': re.compile('^btl')}).string
    publisher = nodes[5].find('a').string
    # print date, '|', title, '|', size, '|', seedNum, '|', DownloadNum, '|', publisher
    open('ktxp.txt', 'a').write((date + '|' + title + '|' + size + '|' + seedNum + '|' + DownloadNum + '|' + publisher + '\n').encode('utf-8'))

if __name__ == '__main__':
    main()