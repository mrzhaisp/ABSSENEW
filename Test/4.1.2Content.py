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

    def get_poinfo(self):
        print self.test_normal()
        for orderid in self.test_normal():
            print orderid
            pram = {'a': orderid}
            sql = "select  req_content from abs_product.pc_syncproduct_log   where orderid  = :a order by company_num "
            content = self.od.Selec_Dtae(sql, pram)
            # print content
            pram = []
            for i in content:
                text = i[0].read()
                pram.append(text)
                m4 = "".join(pram)
                m5 = json.loads(m4)
            # print type(m5)
            # unicode转化为字符串 m6为字符串
            m6 = (m5["content"]).encode("utf-8")
            # print  'new is ',type(m6),m6
            #字符串反序列化成字典但是里面有unicode
            poistr = json.loads(m6)
            poidict_unicode = poistr["poInfo"]
            poidict = json.dumps(poidict_unicode,encoding="UTF-8",ensure_ascii=False)
            print poidict
        self.od.closeData()
if __name__ == '__main__':
    sy = ProductInfo()
    # sy.test_normal()
    sy.get_poinfo()
