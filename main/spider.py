# coding:utf-8
__author__ = 'hano'
import urllib2
import re
import BeautifulSoup as bs


def main():
    get_web_content("http://bt.ktxp.com/today.html#1")


def get_web_content(url):
    if url is None:
        return "the url is null !"
    else:
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req)
        web_content = resp.read()
        soup = bs.BeautifulSoup(web_content)
        divs = soup.findAll('div', attrs={'class': 'item-box round-corner space-bottom'})
        for div in divs:
            # this div contains the section title(like music/game ..) and the list of resource
            open('ktxp.txt', 'a').write("========= section " + div.find('h2').contents[0].string.encode('utf-8') + " begin =========\n")
            tbody = div.find('table').find('tbody')
            res_list = tbody.findAll('tr')
            for item in res_list:
                analyst_ktxp_item(item)
            open('ktxp.txt', 'a').write("========= section end =========\n\n")
        return divs


def analyst_ktxp_item(item):
    # ================== the ktxp res item strut ============================
    # date|resource title    |resource size|seed nums      |download nums  |publisher
    # td  |td(ltext ttitle)/a|      td     |td(class/bts-2)|td(class/btl-1)|td/a(class/team-name)
    # ================== end ================================================
    nodes = item.findAll('td')
    date = nodes[0].string
    title = item.find('td', attrs={'class': 'ltext ttitle'}).contents[1].string
    size = nodes[2].string
    seed_num = item.find('td', attrs={'class': re.compile('^bts')}).string
    download_num = item.find('td', attrs={'class': re.compile('^btl')}).string
    publisher = nodes[5].find('a').string
    open('ktxp.txt', 'a').write((date + '|' + title + '|' + size + '|' + seed_num + '|' + download_num + '|' + publisher + '\n').encode('utf-8'))

if __name__ == '__main__':
    main()