import requests, json
base_url="https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
response=requests.get(base_url)
info=json.loads(response.text)
sss=input("請輸入行政區")
rrr=info["retVal"]
zzz=len(rrr)
for i in range (1,zzz):
    num=("%04d"%i)
    if num in info["retVal"]:
        if info["retVal"][num]["sarea"]==sss:
            aaa=info["retVal"][num]["sna"]
            bbb=aaa.split("(")
            print("行政區:%s"%info["retVal"][num]["sarea"])
            print("地點:%s"%bbb[0])
            print("總共車輛:%s"%info["retVal"][num]["tot"])
            print("剩餘車輛:%s\n"%info["retVal"][num]["sbi"])
    else:
        continue