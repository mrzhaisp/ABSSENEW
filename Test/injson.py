#coding=utf-8
from Commonlib.OraDb import OraDb
import json
class Getinfo():
    def __init__(self):
        self.od = OraDb()

    def getInfo(self):
        orderid = "00020190226191449008"
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
        # 字符串反序列化成字典但是里面有unicode
        poistr = json.loads(m6)
        poidict_unicode = poistr["poInfo"]
        poiunicode = json.dumps(poidict_unicode, encoding="UTF-8", ensure_ascii=False)
        datejson = json.loads(poiunicode)
        print type(datejson),datejson

g = Getinfo()
g.getInfo()






