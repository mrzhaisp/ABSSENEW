#coding=utf-8
from Commonlib.OraDb import OraDb
from Commonlib.LogIni import LogIni
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Productindesc():
    def __init__(self):
        self.ora = OraDb()
        self.lo = LogIni()
        self.base_url  = "http://10.248.50.225:8990/api/v2/sync/BBOSS/syncProduct2Province?offerNum=50013"

    def test_normal(self):
        """拿到所有下发的orderid"""
        response = requests.get(self.base_url)
        respcont = response.text
        # print (type(respcont))  返回报文为unicode  转化为字符串
        respcstr = respcont.encode("utf-8")
        #respcstr 字符串转化为字典
        respdict = eval(respcstr)
        #取出data里的orderid
        ordernum = respdict["data"]
        return ordernum

    def Get_compn_desc(self):
        '''拿到下发的poorderid  然后根据sql查出描述不包含Success的'''
        compnum = []
        errordesc = []
        listordernum=self.test_normal()
        for ordnum in listordernum:
            # print 'This is province order number %s' % ordnum
            # ordnum = str(listordernum)
            pram = {'amp': ordnum}
            sql = "select a.company_num, a.rspdesc  from abs_product.pc_syncproduct_log a where a.orderid  in :amp and a.rspdesc  not like '%sucess%' and a.rspdesc not like '%Success%'   and a.rspdesc not like '%success%' order by a.company_num"
            compdesc = self.ora.Selec_Dtae(sql,pram)
            for row in compdesc:
                # print row[0],row[1]
                compnum.append(row[0])
                errordesc.append(row[1])
        #拿到组合成的省编码和报错信息 组合成一个字典
        dictcompdescascii = dict(map(lambda x,y:[x,y],compnum,errordesc))
        # dictcompdesc = (zip(compnum,errordesc))
        #转成字典后汉字出现二进制  需要转化成utf-8
        dictcompdescunicode = json.dumps(dictcompdescascii,encoding="UTF-8",ensure_ascii=False)
        print type(dictcompdescunicode),dictcompdescunicode
        self.lo.log(dictcompdescunicode)
        #关闭数据库连接
        self.ora.closeData()

po = Productindesc()
po.Get_compn_desc()

















