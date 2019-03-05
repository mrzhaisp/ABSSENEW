#coding=utf-8
from Commonlib.OraDb import OraDb
from Commonlib.LogIni import LogIni
import requests,datetime,time
import json
import importlib,sys
importlib.reload(sys)
import csv
class Productindesc():
    """测试test  写入csv文件"""
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
        allist = []
        # listordernum=self.test_normal()
        listordernum = ['00020190226191449008',  '10020190226191449010',
                             '20020190226191450715', '21020190226191450845',  '22020190226191453865',  '23020190226191453082',     '24020190226191453309',
                             '25020190226191454941',  '27020190226191454046',    '28020190226191454787',   '29020190226191455777',  '31120190226191455523',
                             '35120190226191456364',  '37120190226191456002',   '43120190226191457807', '45120190226191457193',      '47120190226191457463',
                             '53120190226191458906', '55120190226191500036',   '57120190226191500199',   '59120190226191502522',    '73120190226191503332',
                             '77120190226191503658','79120190226191503226','85120190226191504918','87120190226191505711','89120190226191505431','89820190226191506063',
                             '93120190226191507128','95120190226191507450','97120190226191528876','99120190226191529111']
        for ordnum in listordernum:
            pram = {'amp': ordnum}
            sql = "select a.company_num, a.rspdesc ,a.res_content from abs_product.pc_syncproduct_log a where a.orderid  in :amp and a.rspdesc  not like '%sucess%' and a.rspdesc not like '%Success%'   and a.rspdesc not like '%success%' order by a.company_num"
            compdesc = self.ora.Selec_Dtae(sql,pram)
            for row in compdesc:
                # print row[0],row[1]
                #拿到省编码和描述
                company_num = (row[0])
                rspdesc = (row[1])
                #取到r返回报文的值
                responsedesc = json.loads((row[2]).read())
                responsedescinfo = responsedesc['response']
                #取到最后response
                res_content = json.dumps(responsedescinfo, ensure_ascii=False)
                posito = {
                    '省编码':company_num,
                    '描述信息': rspdesc,
                    '返回报文': res_content,
                }
                allist.append(posito)
        return allist
        #关闭数据库连接
        self.ora.closeData()

    def writeCsv(self):
        self.headers = {"省编码","描述信息","返回报文"}
        posit = self.Get_compn_desc()
        # print(posit)
        #把取到的内容  写入到csv
        with open('../TestReport/report.csv', 'a',newline='',encoding="gbk") as f:
            writer = csv.DictWriter(f,self.headers)
            writer.writeheader()
            writer.writerows(posit)


po = Productindesc()
po.writeCsv()
















