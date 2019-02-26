#coding=utf-8
import cx_Oracle as oracle
class OraDb():
    def __init__(self):
        # 创建链接
        self.db = oracle.connect('abs_product', 'bboss_ju', '10.248.50.218:1521/abs2')
        # 创建游标
        self.cs1 = self.db.cursor()

    def Selec_Dtae(self,sql,Twob):
        try:
            cms = self.cs1.execute(sql,Twob)
            return cms
        except Exception ,e:
            print e

        # 关闭数据库连接
    def closeData(self):
        self.cs1.close()
        self.db.close()

