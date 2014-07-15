__author__ = 'hano'
# coding:utf-8
import urllib2

import BeautifulSoup as bs


def main():
    print getWebContent("http://bt.ktxp.com/today.html#1")
    # print getWebContent("http://www.baidu.com")


def getWebContent(url):
    if (url == None):
        return "the url is null !"
    else:
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req)
        webContent = resp.read()
        soup = bs.BeautifulSoup(webContent)
        length = len(soup.findAll('td', attrs={'class': 'ltext ttitle'}))
        return length


if __name__ == '__main__':
    main()