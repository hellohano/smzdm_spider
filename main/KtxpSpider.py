# coding:utf-8
__author__ = 'hano'
import urllib2
import re

import BeautifulSoup as bs

import KtxpItem as ktxp


ktxp_today = "http://bt.ktxp.com/today.html#1"
ktxp_domain = 'http://bt.ktxp.com'
ktxp_all_res_link = {}
ktxp_all_link = []


def main():
    ktxp_all_res_link[1] = '/index-1.html'
    # get_ktxp_all_res(ktxp_all_res_link[1], 1)
    get_ktxp_today_res(ktxp_today)


def get_web_content_to_beautifulsoup(url):
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    web_content = resp.read()
    return bs.BeautifulSoup(web_content)


def get_ktxp_all_res(url, pagenum):
    ktxpurl = ktxp_domain + url
    soup = get_web_content_to_beautifulsoup(ktxpurl)
    pages = soup.find('div', {'class': 'pages clear space-bottom'})
    current_node = pages.find('span', {'class': 'current'})
    # page_nodes = pages.findAll('a', {'href': re.compile('^/index-')})
    page_nodes = pages.findAll('a', attrs={'class': None}, href=re.compile('^/index-'))
    for node in page_nodes:
        print 'node is ==', node
        nodenum = int(node.string)
        if nodenum > pagenum:
            if not ktxp_all_res_link.has_key(nodenum):
                ktxp_all_link.append(node['href'])
                ktxp_all_res_link[int(node.string)] = node['href']
    print 'all url is =', ktxp_all_link
    del ktxp_all_res_link[pagenum]
    print 'search url is =', ktxp_all_res_link
    if len(ktxp_all_res_link.keys()) > 0:
        get_ktxp_all_res(ktxp_all_res_link[pagenum + 1], pagenum + 1)
    else:
        for link in ktxp_all_link:
            open('ktxp_all_res_url.txt', 'a').write(link + '\n')


def get_ktxp_today_res(url):
    if url is None:
        return "the url is null !"
    else:
        soup = get_web_content_to_beautifulsoup(url)
        divs = soup.findAll('div', attrs={'class': 'item-box round-corner space-bottom'})
        for div in divs:
            # this div contains the section title(like music/game ..) and the list of resource
            open('ktxp.txt', 'a').write("========= section " + div.find('h2').contents[0].string.encode('utf-8')
                                        + " begin =========\n")
            tbody = div.find('table').find('tbody')
            res_list = tbody.findAll('tr')
            for item in res_list:
                analyst_ktxp_today_item(item)
            open('ktxp.txt', 'a').write("========= section end =========\n\n")
        return divs


def analyst_ktxp_today_item(item):
    # ================== the ktxp res item strut ============================
    # date|resource title    |resource size|seed nums      |download nums  |publisher
    # td  |td(ltext ttitle)/a|      td     |td(class/bts-2)|td(class/btl-1)|td/a(class/team-name)
    # ================== end ================================================
    nodes = item.findAll('td')
    # if only have one node, it will be '没有任何资源'
    if len(nodes) != 1:
        ktxp_item = ktxp.KtxpItem
        ktxp_item.date = nodes[0].string
        ktxp_item.title = item.find('td', attrs={'class': 'ltext ttitle'}).contents[1].string
        ktxp_item.size = nodes[2].string
        ktxp_item.seed_num = item.find('td', attrs={'class': re.compile('^bts')}).string
        ktxp_item.download_num = item.find('td', attrs={'class': re.compile('^btl')}).string
        ktxp_item.publisher = nodes[5].find('a').string
        open('ktxp.txt', 'a').write(ktxp.KtxpItem.print_item(ktxp_item))


if __name__ == '__main__':
    main()