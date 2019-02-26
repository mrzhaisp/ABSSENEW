#codingutf-8
from Commonlib.OraDb import OraDb

class Productindesc():
    def __init__(self):
        self.ora = OraDb()

    def Get_compn_desc(self):
        listordernum = ['00020190226191449008',  '10020190226191449010',
                             '20020190226191450715', '21020190226191450845',  '22020190226191453865',  '23020190226191453082',     '24020190226191453309',
                             '25020190226191454941',  '27020190226191454046',    '28020190226191454787',   '29020190226191455777',  '31120190226191455523',
                             '35120190226191456364',  '37120190226191456002',   '43120190226191457807', '45120190226191457193',      '47120190226191457463',
                             '53120190226191458906', '55120190226191500036',   '57120190226191500199',   '59120190226191502522',    '73120190226191503332',
                             '77120190226191503658','79120190226191503226','85120190226191504918','87120190226191505711','89120190226191505431','89820190226191506063',
                             '93120190226191507128','95120190226191507450','97120190226191528876','99120190226191529111']
        # for ordnum in listordernum:
        ordnum = str(listordernum)
        pram = {'amp': ordnum}
        sql = "select a.company_num, a.rspdesc  from abs_product.pc_syncproduct_log a where a.orderid  in :amp and a.rspdesc  not like '%sucess%' and a.rspdesc not like '%Success%'   and a.rspdesc not like '%success%' order by a.company_num"
        compdesc = self.ora.Selec_Dtae(sql,pram)
        print compdesc

po = Productindesc()
po.Get_compn_desc()

















