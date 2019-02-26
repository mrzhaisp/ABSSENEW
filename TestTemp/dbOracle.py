#! /usr/bin/env python
#encoding=utf-8
"""
oracle数据库的读写操作
"""

import cx_Oracle as oracle
import sys
import json


class DB():
    #初始化数据库，对于oracle数据库，只需要提供instancename即可
    def __init__(self,InstanceName = None):
        self.InstanceName = InstanceName
        self.cursor = None   #创建一个数据库游标，用于每次执行

    #连接数据库
    def ConnDB(self):
        try:
            self.db = oracle.connect(self.InstanceName)
        except Exception as e:
            sys.stderr(e)

    #查询数据库，根据orderid和创建时间查询下发给各省的数据是否正确
    def Select_One_Record(self,query,params):
        #连接数据库
        try:
            self.ConnDB()
            #创建cursor
            self.cursor = self.db.cursor()
            self.cursor.execute(query,params)
            for row in self.cursor:
                properties = row[9]
                data = json.loads(str(properties))
                # print(data)
                content = json.loads(data['content'])
                # print(content)
                rsp_code  = row[6]
                rsp_des = row[7]
                prov_code = row[11]

            # query_result = self.cursor.fetchone()
            self.cursor.close()
            self.db.close()
            return content,rsp_code,rsp_des,prov_code
        except Exception as e:
            sys.stderr(e)
            self.cursor.close()
            self.db.close()


    def SelectOneRecord(self,query,params):
        #连接数据库
        try:
            self.ConnDB()
            #创建cursor
            self.cursor = self.db.cursor()
            self.cursor.execute(query,params)
            col = self.cursor.description   #获取查询的列名
            query_result = self.cursor.fetchone() #获取返回结果
            self.cursor.close()
            self.db.close()
            return col,query_result
        except Exception as e:
            sys.stderr(e)
            self.cursor.close()
            self.db.close()

if __name__ == '__main__':
    InstanName = 'abs_product/bboss_ju@10.248.50.218:1521/abs2'
    #传入的sql语句需要用双引号，不能用单引号
    query = "select * from abs_product.pc_syncproduct_log a where a.orderid = :a and to_char(a.create_date,'YYYYMMDD') = :b"
    OrderId = '20020190117101810916'
    createdate = '20190117'
    #多个参数传递，需要通过字典的方式，参数作为key值
    params = {'a':OrderId,'b':createdate}
    product_db = DB(InstanName)
    content, rsp_code, rsp_des, prov_code = product_db.Select_One_Record(query,params)
    #
    # poinfo_keys = content['poInfo'].keys().upper()
    poinfo_dict = {k.upper():v for k,v in content['poInfo'].items()}
    # print(poinfo_dict)
    # pe.loadWorkBook('./properties_result.xlsx')
    query1 = "select po.offer_num poSpecNumber,po.offer_name poSpecName,po.status,to_char(po.start_date,'YYYYMMDDHH24MMSS') startDate,to_char(po.end_date,'YYYYMMDDHH24MMSS') endDate,pi.describe description,po.isautoconfig,po.action,to_char(po.potimestamp,'YYYYMMDDHH24MMSS') potimestamp,po.productBICode from pc_offer po inner join pc_offer_info pi on pi.offer_num = po.offer_num where po.offer_num = :a"

    param ={'a':'50013'}
    collist,result = product_db.SelectOneRecord(query1,param)
    list_a = []
    for i in range(len(collist)):
        list_a.append(collist[i][0])
    # print(list_a)
    result_new = list(result)
    # print(list(result_new))
    dict_new = dict(zip(list_a,result_new))
    print(dict_new)


    #all 函数用于判断当给定一个不为空的可迭代对象之后，如果元素全为真则返回True，否则返回假。即只要存在为假的元素就返回假。
    try:
        all(item in poinfo_dict.items() for item in dict_new.items())
    except Exception as e:
        print(e)
    #判断数据库表中查询出来的结果是不是包含在接口返回的数据中
    #   assertDictContainsSubset(dict_new,poinfo_dict,'商品信息省返回信息与数据库一致')  assertDictContainsSubset(expect,actual,msg)这个方法在Python27里有，Python3中没有
    # assert set(dict_new.items()).issubset(set(poinfo_dict.items())),'商品信息省返回信息与数据库一致'   #可以通过转成set的方式来判断是不是他的子集
    # print(rsp_code)
    # print(rsp_des)
    # print(prov_code)

    def extractDictFromContent(dict_new,poinfo_dict):
        return dict([(k,poinfo_dict[k]) for k in dict_new.keys() if k in poinfo_dict.keys()])


    s = extractDictFromContent(dict_new,poinfo_dict)
    print(s)
    # assertEqual(dict_new,extractDictFromContent(dict_new,poinfo_dict))


