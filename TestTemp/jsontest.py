#coding=utf-8
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

onCodejson_txt ="""{"status": "A", "startDate": "20180925150900", "poTimeStamp": "20181023141039", "poSpecRatePlans": [], "endDate": "20190925150900", "description": "支持集团客户的中国移动手机号码和固定号码组成跨省、跨域的新V网集团，享受用户间的真实号码互拨优惠", "productBICode": "1111", "enableCompanys": ["000", "100", "200", "210", "220", "230", "240", "250", "270", "280", "290", "311", "351", "371", "431", "451", "471", "531", "551", "571", "591", "731", "771", "791", "851", "871", "891", "898", "931", "951", "971", "991"], "poSpecNumber": "50013", "chargeItemInfo": [], "products": [{"productBICode": "1111", "productRatePlans": [{"startDate": "20181013151009", "endDate": "20991231231259", "description": "40元/成员，每成员含2000分钟免费国内主叫通话，超出部分按个人资费规则计费，个人支付", "ratePlanType": "1", "ratePlanSort": "2", "ratePlanID": "1657", "action": "1", "parameter": [{"parameterName": "d", "parameterUnit": "09", "parameterNumber": "50000000003"}, {"parameterName": "x", "parameterUnit": "01", "parameterNumber": "50000000001"}, {"parameterName": "y", "parameterUnit": "05", "parameterNumber": "50000000002"}]}, {"startDate": "20181013151009", "endDate": "20991231231259", "description": "20元/成员，每成员含1000分钟免费国内主叫通话，超出部分按个人资费规则计费，个人支付", "ratePlanType": "1", "ratePlanSort": "2", "ratePlanID": "1656", "action": "1", "parameter": [{"parameterName": "d", "parameterUnit": "09", "parameterNumber": "50000000003"}, {"parameterName": "x", "parameterUnit": "01", "parameterNumber": "50000000001"}, {"parameterName": "y", "parameterUnit": "05", "parameterNumber": "50000000002"}]}, {"startDate": "20181013151009", "endDate": "20991231231259", "description": "10元/成员，每成员含500分钟免费国内主叫通话，超出部分按个人资费规则计费，个人支付", "ratePlanType": "1", "ratePlanSort": "2", "ratePlanID": "1655", "action": "1", "parameter": [{"parameterName": "d", "parameterUnit": "09", "parameterNumber": "50000000003"}, {"parameterName": "x", "parameterUnit": "01", "parameterNumber": "50000000001"}, {"parameterName": "y", "parameterUnit": "05", "parameterNumber": "50000000002"}]}], "productAction": "1", "productSpecCharacters": [{"productSpecCharacterNumber": "50013010001", "name": "集团客户联系人"}, {"productSpecCharacterNumber": "50013010002", "name": "集团客户联系电话"}, {"productSpecCharacterNumber": "50013010003", "name": "集团客户联系人邮箱"}, {"productSpecCharacterNumber": "50013010004", "name": "集团客户简称"}, {"productSpecCharacterNumber": "50013010005", "name": "折扣率（0-100%）"}, {"productSpecCharacterNumber": "50013010006", "name": "统付类型", "valueSource": ["0"]}, {"productSpecCharacterNumber": "50013010007", "name": "最大成员数"}], "productSpec": {"status": "A", "productSpecNumber": "5001301", "description": "集团新V网", "productSpecName": "集团新V网"}, "productChargeItemInfo": [{"chargeCode2": "5001301", "chargeCode3": "18", "taxRate": "6", "chargeCode1": "50013", "chargeName1": "集团V网（全国版）", "chargeName2": "集团新V网", "chargeName3": "套餐费", "chargeType": "2", "chargeBICode": "111"}, {"chargeCode2": "5001301", "chargeCode3": "68", "taxRate": "6", "chargeCode1": "50013", "chargeName1": "集团V网（全国版）", "chargeName2": "集团新V网", "chargeName3": "调帐套餐费", "chargeType": "2", "chargeBICode": "111"}]}], "isAutoConfig": "0", "action": "1", "poSpecName": "集团V网（全国版）"}"""
print type(onCodejson_txt),onCodejson_txt
datajson = eval(onCodejson_txt)
# print type(datajson),datajson
# datajsondict = json.dumps(datajson, encoding="utf-8", ensure_ascii=False)
print type(datajson),datajson

for jiedian,zijiedian in datajson.items():
    print jiedian
    # for iszijiedina  ,value in zijiedian.items():
    #     print iszijiedina

















