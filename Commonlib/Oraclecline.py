#coding=utf-8
import cx_Oracle as oracle

class Oraclecline():
    def __init__(self):
        # 创建链接
        self.db = oracle.connect('abs_product', 'bboss_ju', '10.248.50.218:1521/abs2')
        # 创建游标
        self.cursor = self.db.cursor()

    def dateSelec(self,sql,param):
        try:
            contentlist = self.cursor.execute(sql,param)
            # self.cursor.close()
            # self.db.close()
            return contentlist
        except Exception,e:
            print(e)
        # finally:
        #     self.cursor.close()
        #     self.db.close()

    #关闭数据库连接
    def closeData(self):
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    dm = Oraclecline()
    list11 = ['00020190225131923915', '10020190225131923178', '20020190225131929817', '21020190225131929629',
              '22020190225131931415', '23020190225131932730', '24020190225131932333', '25020190225131932166',
              '27020190225131933039', '28020190225131933499', '29020190225131934428', '31120190225131934748',
              '35120190225131935324', '37120190225131935175', '43120190225131936711', '45120190225131936257',
              '47120190225131936426', '53120190225131939315', '55120190225131939583', '57120190225132039047',
              '59120190225132040929', '73120190225132040436', '77120190225132040116', '79120190225132041120',
              '85120190225132041872', '87120190225132041288', '89120190225132042847', '89820190225132043236',
              '93120190225132043310', '95120190225132044913', '97120190225132104945', '99120190225132105593']
    int_list = str(list11)
    #拿到所有的省编码和内容
    alllist = []
    for li in list11:
        # print li
        param = {'a': li}
        sql = "select   req_content from abs_product.pc_syncproduct_log   where orderid  in :a   order by company_num"
        list3 =dm.dateSelec(sql,param)
        # print list3
        alllist.append(list3)
    print alllist


    # dm.closeData()

















