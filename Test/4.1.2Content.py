#coding=utf-8
#__author__ = 'zgd'
from Commonlib.OraDb import OraDb
import requests
import json
import time
import importlib,sys
importlib.reload(sys)
class ProductInfo():
    """测试test"""
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
        # print (self.test_normal())
        # for orderid in self.test_normal():
        # alist = ['00020190304163205555', '10020190304163206476', '20020190304163209531', '21020190304163210288', '22020190304163220612', '23020190304163221695', '24020190304163221199', '25020190304163221047', '27020190304163251852', '28020190304163252499', '29020190304163252877', '31120190304163253362', '35120190304163254013', '37120190304163255141', '43120190304163255477', '45120190304163255880', '47120190304163255444', '53120190304163300644', '55120190304163302031', '57120190304163303989', '59120190304163303841', '73120190304163304344', '77120190304163304719', '79120190304163305889', '85120190304163306469', '87120190304163306048', '89120190304163314128', '89820190304163315429', '93120190304163315111', '95120190304163316629', '97120190304163338723', '99120190304163339314']
        alist = ['00020190304163205555']
        for orderid in alist:
            print (orderid)
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
            poidict = json.dumps(poidict_unicode,ensure_ascii=False)
            print (poidict)
        self.od.closeData()
        return poidict

if __name__ == '__main__':
    sy = ProductInfo()
    # sy.test_normal()
    sy.get_poinfo()
