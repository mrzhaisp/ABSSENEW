#coding=utf-8
#__author__ = 'zgd'
from Commonlib.OraDb import OraDb
import requests
import json
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class ProductInfo():
    """4.1.商产品规格信息同步"""
    def __init__(self):
        self.base_url  = "http://10.248.50.225:8990/api/v2/sync/BBOSS/syncProduct2Province?offerNum=50013"
        self.od = OraDb()

    def test_normal(self):
        response = requests.get(self.base_url)
        respcont = response.text
        # print (type(respcont))  返回报文为unicode  转化为字符串
        respcstr = respcont.encode("utf-8")
        #respcstr 字符串转化为字典
        respdict = eval(respcstr)
        #取出data里的orderid
        ordernum = respdict["data"]
        return ordernum

    def get_orderinfo(self):
        info_list = []
        li_orderid = self.test_normal()
        print type(li_orderid),"list1 is %s" %li_orderid
        int_orderid = int(li_orderid)
        print type(int_orderid)
        # print orderid
        pram = {'a': li_orderid}
        sql = "select  req_content from abs_product.pc_syncproduct_log   where orderid  in :a "
        content = self.od.Selec_Dtae(sql, pram)
        info_list.append(content)
        print info_list


if __name__ == '__main__':
    po = ProductInfo()
    po.test_normal()
    po.get_orderinfo()