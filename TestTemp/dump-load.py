import json
import jsonpath
# json文件发送形式
SendRegisterVerificationCodejson_txt = """{
	"poInfo": {
		"action": "1",
		"poSpecNumber": "50013",
		"poSpecName": "集团V网（全国版）",
		"status": "A",
		"startDate": "20180925150900",
		"endDate": "20190925150900",
		"description": "支持集团客户的中国移动手机号码和固定号码组成跨省、跨域的新V网集团，享受用户间的真实号码互拨优惠",
		"enableCompanys": ["000", "100", "200", "210", "220", "230", "240", "250", "270", "280", "290", "311", "351", "371", "431", "451", "471", "531", "551", "571", "591", "731", "771", "791", "851", "871", "891", "898", "931", "951", "971", "991"],
		"poSpecRatePlans": [],
		"products": [{
			"productSpec": {
				"productSpecNumber": "5001301",
				"productSpecName": "集团新V网",
				"status": "A",
				"description": "集团新V网"
			},
			"productAction": "1",
			"productRatePlans": [{
				"ratePlanID": "1657",
				"description": "40元/成员，每成员含2000分钟免费国内主叫通话，超出部分按个人资费规则计费，个人支付",
				"ratePlanSort": "2",
				"ratePlanType": "1",
				"startDate": "20181013151009",
				"endDate": "20991231231259",
				"action": "1",
				"parameter": [{
					"parameterNumber": "50000000003",
					"parameterName": "d",
					"parameterUnit": "09"
				}, {
					"parameterNumber": "50000000001",
					"parameterName": "x",
					"parameterUnit": "01"
				}, {
					"parameterNumber": "50000000002",
					"parameterName": "y",
					"parameterUnit": "05"
				}]
			}, {
				"ratePlanID": "1656",
				"description": "20元/成员，每成员含1000分钟免费国内主叫通话，超出部分按个人资费规则计费，个人支付",
				"ratePlanSort": "2",
				"ratePlanType": "1",
				"startDate": "20181013151009",
				"endDate": "20991231231259",
				"action": "1",
				"parameter": [{
					"parameterNumber": "50000000003",
					"parameterName": "d",
					"parameterUnit": "09"
				}, {
					"parameterNumber": "50000000001",
					"parameterName": "x",
					"parameterUnit": "01"
				}, {
					"parameterNumber": "50000000002",
					"parameterName": "y",
					"parameterUnit": "05"
				}]
			}, {
				"ratePlanID": "1655",
				"description": "10元/成员，每成员含500分钟免费国内主叫通话，超出部分按个人资费规则计费，个人支付",
				"ratePlanSort": "2",
				"ratePlanType": "1",
				"startDate": "20181013151009",
				"endDate": "20991231231259",
				"action": "1",
				"parameter": [{
					"parameterNumber": "50000000003",
					"parameterName": "d",
					"parameterUnit": "09"
				}, {
					"parameterNumber": "50000000001",
					"parameterName": "x",
					"parameterUnit": "01"
				}, {
					"parameterNumber": "50000000002",
					"parameterName": "y",
					"parameterUnit": "05"
				}]
			}],
			"productSpecCharacters": [{
				"productSpecCharacterNumber": "50013010001",
				"name": "集团客户联系人"
			}, {
				"productSpecCharacterNumber": "50013010002",
				"name": "集团客户联系电话"
			}, {
				"productSpecCharacterNumber": "50013010003",
				"name": "集团客户联系人邮箱"
			}, {
				"productSpecCharacterNumber": "50013010004",
				"name": "集团客户简称"
			}, {
				"productSpecCharacterNumber": "50013010005",
				"name": "折扣率（0-100%）"
			}, {
				"productSpecCharacterNumber": "50013010006",
				"name": "统付类型",
				"valueSource": ["0"]
			}, {
				"productSpecCharacterNumber": "50013010007",
				"name": "最大成员数"
			}],
			"productChargeItemInfo": [{
				"chargeCode1": "50013",
				"chargeName1": "集团V网（全国版）",
				"chargeCode2": "5001301",
				"chargeName2": "集团新V网",
				"chargeCode3": "18",
				"chargeName3": "套餐费",
				"taxRate": "6",
				"chargeType": "2",
				"chargeBICode": "111"
			}, {
				"chargeCode1": "50013",
				"chargeName1": "集团V网（全国版）",
				"chargeCode2": "5001301",
				"chargeName2": "集团新V网",
				"chargeCode3": "68",
				"chargeName3": "调帐套餐费",
				"taxRate": "6",
				"chargeType": "2",
				"chargeBICode": "111"
			}],
			"productBICode": "1111"
		}],
		"chargeItemInfo": [],
		"isAutoConfig": "0",
		"poTimeStamp": "20181023141039",
		"productBICode": "1111"
	},
	"orderId": "00020190226191449008"
}"""
date_json = json.loads(SendRegisterVerificationCodejson_txt)
# print(date_json)
print("*" * 10)
# poInfo = jsonpath.jsonpath(date_json,"poInfo")
# print(poInfo)


# 遍历json文件所有的key对应的value
dic = {}
def json_txt(dic_json):
    if isinstance(dic_json, dict):  # 判断是否是字典类型isinstance 返回True false
        for key in dic_json:
            if isinstance(dic_json[key], dict):  # 如果dic_json[key]依旧是字典类型
                # print("****key--：%s value--: %s" % (key, dic_json[key]))
                json_txt(dic_json[key])
                dic[key] = dic_json[key]
            else:
                # print("****key--：%s value--: %s" % (key, dic_json[key]))
                dic[key] = dic_json[key]


json_txt(date_json)
print("dic ---: " + str(dic))
print(type(dic))
print(dic.keys())
# lsitr = []
# for k,v in dic.items():
    # print(v)
    # lsitr.append(v)
# print(lsitr)


