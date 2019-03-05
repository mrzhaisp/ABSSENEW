#coding=utf-8
from Commonlib.OraDb import OraDb
from Commonlib.LogIni import LogIni
import requests,datetime,time
import json
import importlib,sys
importlib.reload(sys)

class Productindesc():
    def __init__(self):
        self.ora = OraDb()
        self.lo = LogIni()
        self.base_url  = "http://10.248.50.225:8990/api/v2/sync/BBOSS/syncProduct2Province?offerNum="

    def test_normal(self):
        """拿到所有下发的orderid"""
        offnumber =input (u"请输出商产品规格编码")
        baseurl = self.base_url + offnumber
        # print baseurl
        stsrt_time = "START_" + u'下发产品规格offernumber'+ '%s' %(offnumber ) +"*" * 20 + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') +"*" * 20
        self.lo.log(stsrt_time)
        response = requests.get(baseurl)
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
        listordernum=self.test_normal()
        for ordnum in listordernum:
            # print 'This is province order number %s' % ordnum
            # ordnum = str(listordernum)
            pram = {'amp': ordnum}
            sql = "select a.company_num, a.rspdesc ,a.res_content from abs_product.pc_syncproduct_log a where a.orderid  in :amp and a.rspdesc  not like '%sucess%' and a.rspdesc not like '%Success%'   and a.rspdesc not like '%success%' order by a.company_num"
            compdesc = self.ora.Selec_Dtae(sql,pram)
            for row in compdesc:
                # print row[0],row[1]
                compnum.append(row[0])
                compnum.append(row[1])
                #取到res_content的值
                responsedesc = json.loads((row[2]).read())
                # responsedesc = json.dumps(responsedesc, encoding="UTF-8", ensure_ascii=False)
                responsedescinfo = responsedesc['response']
                # print type(responsedescinfo),responsedescinfo
                result = json.dumps(responsedescinfo, ensure_ascii=False)
                # print result
                compnum.append(result)
                compnum.append('                            ')
        # print type(compnum),compnum
        #拿到组合成的省编码和报错信息 组合成一个字典
        # dictcompdescascii = dict(map(lambda x,y:[x,y],compnum,errordesc))
        # dictcompdesc = (zip(compnum,errordesc))
        # #转成字典后汉字出现二进制  需要转化成utf-8
        # dictcompdescunicode = json.dumps(dictcompdescascii,encoding="UTF-8",ensure_ascii=False)
        # print type(dictcompdescunicode),dictcompdescunicode
        #输出到日志
        self.lo.log(compnum)
        end_time = "END_"  +"*"*20,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"*"*20
        self.lo.log(end_time)
        print (compnum)
        #关闭数据库连接
        self.ora.closeData()

po = Productindesc()
po.Get_compn_desc()

















