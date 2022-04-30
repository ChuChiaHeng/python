import requests, json
base_url="https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
response=requests.get(base_url)
info=json.loads(response.text)
for i in range (1,11):
    num=("%04d"%i)
    aaa=info["retVal"][num]["sna"]
    bbb=aaa.split("(")
    print("地點:%s"%bbb[0])
    print("總共車輛:%s"%info["retVal"][num]["tot"])
    print("剩餘車輛:%s\n"%info["retVal"][num]["sbi"])