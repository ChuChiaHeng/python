import requests, json
import matplotlib.pyplot as plt
base_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
response = requests.get(base_url)
info = response.json()
data = []
position = []
total_bike = []
remain_bike = []
area = input("請輸入地區:")
for num in info["retVal"]:
    if info["retVal"][num]["sarea"] == area:
        position.append(info["retVal"][num]["sna"].split("(")[0])
        total_bike.append(int(info["retVal"][num]["tot"]))
        remain_bike.append(int(info["retVal"][num]["sbi"]))
A=plt.bar(position[:8],total_bike[:8],label="全部停車格")
B=plt.bar(position[:8],remain_bike[:8],label="剩下車輛")
plt.legend(loc=1)
plt.show()
