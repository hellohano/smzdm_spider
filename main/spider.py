__author__ = 'hano'
# coding:utf-8
import urllib2

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
            print "========= section ", divs.index(div), div.find('h2').contents[0].string, " begin ========="
            tbody = div.find('table').find('tbody')
            resList = tbody.findAll('tr')
            for item in resList:
                analystKTXPItem(item)
            print "========= section ", divs.index(div), " begin ========="
        return divs


def analystKTXPItem(item):
    # ================== the ktxp res item strut ============================
    # date|resource title    |resource size|seed nums      |download nums  |publisher
    # td  |td(ltext ttitle)/a|      td     |td(class/bts-2)|td(class/btl-1)|td/a(class/team-name)
    # ================== end ================================================
    date = item.contents[0]
    title = item.find('td', attrs={'class': 'ltext ttitle'}).contents[1].string
    size = item.contents[2].string
    seedNum = item.find('td', attrs={'class': 'bts-2'})
    DownloadNum = item.find('td', attrs={'class': 'btl-1'})
    publisher = item.contents[5].find('a', attrs={'class': 'team-name'})
    print date, '|', title, '|', size, '|', seedNum, '|', DownloadNum, '|', publisher


if __name__ == '__main__':
    main()