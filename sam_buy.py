import json
import requests
from time import sleep


# getCapacityData commitPay 接口的request.body和header 都需要修改为自己的！

# 全局变量定义 无需传参 会在getCapacityData中赋值
startRealTime = ''
endRealTime = ''

# 修改点1： /getCapacityData抓包 填写下面值
longitude = ''
latitude = ''
deviceid = ''
authtoken = ''
# 修改点2： /commitPay 抓包填写下面值
# 把getCapacityData接口的response.body里一些关于库存的true或false修改一下就可以进入到commitPay方法获取trackinfo和data
# 关于库存修改： timeISFull=false, timeISFull=false,disable=true 即可选择配送时间 进行下单获得commitPay的参数
trackinfo= ''


# 有能力的可以自行修改该方法，联调order方法
def getUserCart():
    myUrl = 'https://api-sams.walmartmobile.cn/api/v1/sams/trade/cart/getUserCart'
    data = {
        # YOUR SELF
    }
    headers = {
        'Host': 'api-sams.walmartmobile.cn',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'Content-Type': 'application/json;charset=UTF-8',
        'Content-Length': '704',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'SamClub/5.0.45 (iPhone; iOS 15.4; Scale/3.00)',
        'device-name': 'iPhone14,3',
        'device-os-version': '15.4',
        'device-id': deviceid,
        'latitude': latitude,
        'track-info': trackinfo,
        'device-type': 'ios',
        'auth-token': authtoken,
        'app-version': '5.0.45.1'

    }
    try:
        ret = requests.post(url=myUrl, headers=headers, data=json.dumps(data))
        print(ret.text)
#         myRet = json.loads(ret.text)
#         # print(myRet['data'].get('capcityResponseList')[0])
#         normalGoodsList = (myRet['data'].get('floorInfoList')[0].get('normalGoodsList'))
#         # time_list = myRet['data'].get('capcityResponseList')[0].get('list')
#         goodlist = []
#         for i in range(0, len(normalGoodsList)):
#             spuId = normalGoodsList[i].get('spuId')
#             goodlist.append(spuId)

    except Exception as e:
        print('getUserCart [Error]: ' + str(e))

def getCapacityData():
    global startRealTime
    global endRealTime

    myUrl = 'https://api-sams.walmartmobile.cn/api/v1/sams/delivery/portal/getCapacityData'
    data = {
        # 修改点3：填自己的
        # "perDateList":["2022-03-30","2022-03-31","2022-04-01","2022-04-02","2022-04-03","2022-04-04","2022-04-05"],"storeDeliveryTemplateId":"1099860739333462"
    }
    headers = {
        'Host': 'api-sams.walmartmobile.cn',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'Content-Type': 'application/json;charset=UTF-8',
        'Content-Length': '156',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'SamClub/5.0.45 (iPhone; iOS 15.4; Scale/3.00)',
        'device-name': 'iPhone14,3',
        'device-os-version': '15.4',
        'device-id': deviceid,
        'latitude': latitude,
        'device-type': 'ios',
        'auth-token': authtoken,
        'app-version': '5.0.45.1'

    }
    try:
        ret = requests.post(url=myUrl, headers=headers, data=json.dumps(data))
        # print(ret.text)
        myRet = json.loads(ret.text)
        print(myRet['data'].get('capcityResponseList')[0])
        status = (myRet['data'].get('capcityResponseList')[0].get('dateISFull'))
        time_list = myRet['data'].get('capcityResponseList')[0].get('list')
        for i in range(0,len(time_list)):
            if not time_list[i].get('timeISFull'):
                startRealTime = time_list[i].get('startRealTime')
                endRealTime = time_list[i].get('endRealTime')
                # print(startRealTime)
                print('【成功】获取配送时间')
                order(startRealTime, endRealTime)
    except Exception as e:
        print('getCapacityData [Error]: ' + str(e))
        return False


def order(startRealTime,endRealTime):
    global index
    print('下单：'+startRealTime)

    myUrl = 'https://api-sams.walmartmobile.cn/api/v1/sams/trade/settlement/commitPay'
    data = {
          # 替换自己抓到的，注意true 加上''单引号
#         # 修改点4：修改 expectArrivalTime为startRealTime ； expectArrivalEndTime 为endRealTime
#         "goodsList":[{"isSelected":'true',"quantity":1,"spuId":"1489392","storeId":"5103"},
#                          {"isSelected":'true',"quantity":1,"spuId":"12422274","storeId":"5103"},
#                          {"isSelected":'true',"quantity":1,"spuId":"24383389","storeId":"5103"},
#                          {"isSelected":'true',"quantity":1,"spuId":"4137707","storeId":"5103"}],
#             "invoiceInfo":{},"cartDeliveryType":1,"floorId":1,"amount":"23220","purchaserName":"",
#              # 修改点4中的一项注意修改"expectArrivalTime":startRealTime,"expectArrivalEndTime":endRealTime
#             "settleDeliveryInfo":{"expectArrivalTime":startRealTime,"expectArrivalEndTime":endRealTime,"deliveryType":0},
#         "tradeType":"APP","purchaserId":"","payType":0,"currency":"CNY","channel":"wechat","shortageId":1,"isSelfPickup":0,"orderType":0,"uid":"18182131375569","appId":"wx5736432dfba","addressId":"142131238","deliveryInfoVO":{"storeDeliveryTemplateId":"1183433472630","deliveryModeId":"1319","storeType":"4"},"remark":"",
#             "storeInfo":{"storeId":"5103","storeType":"4","areaBlockId":"1183123123128374"},
#             "shortageDesc":"其他商品继续配送（缺货商品直接退款）","payMethodId":"1486653332"
       

    }
    headers = {
        'Host': 'api-sams.walmartmobile.cn',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Content-Length': '1617',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'SamClub/5.0.45 (iPhone; iOS 15.4; Scale/3.00)',
        'device-name': 'iPhone14,3',
        'device-os-version': '15.4',
        'device-id': deviceid,
        'longitude': longitude,
        'latitude': latitude,
        'track-info': trackinfo,
        'device-type': 'ios',
        'auth-token': authtoken,
        'app-version': '5.0.45.1'

    }
   try:
        ret = requests.post(url=myUrl, headers=headers, data=json.dumps(data))
        print(ret.text)
        myRet = json.loads(ret.text)
        status = myRet.get('success')
        if status:
            print('【成功】哥，咱家有菜了~')
            import os
            file = r"nb.mp3"
            os.system(file)
            exit()
        else:
            if myRet.get('code') == 'STORE_HAS_CLOSED':
                sleep(60)
                getCapacityData()
            elif myRet.get('code') == 'LIMITED':
                index += 1
                if index > 3:
                    getCapacityData()
                order(startRealTime, endRealTime)
            else:
                getCapacityData()

    except Exception as e:
        print('order [Error]: ' + str(e))
        getCapacityData()
        return False


count = 0
index = 0
while 1:
    count = count + 1
    print(count)
    getCapacityData()
    sleep(6)
