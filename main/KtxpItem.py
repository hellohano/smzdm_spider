# coding:utf-8
__author__ = 'hano'


class KtxpItem:
    date = ''
    category = ''
    title = ''
    size = ''
    seed_num = ''
    download_num = ''
    download_complete = ''
    publisher = ''

    def __init__(self):
        print 'init new ktxp item'

    @staticmethod
    def print_item(self):
        return (self.date + '|' + self.category + '|' + self.title + '|' + self.size + '|' + self.seed_num + '|'
                + self.download_num + '|' + self.download_complete + '|' + self.publisher + '\n').encode('utf-8')