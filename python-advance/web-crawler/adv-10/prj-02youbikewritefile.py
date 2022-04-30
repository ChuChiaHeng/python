import pandas as pd
import requests, json
base_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
response = requests.get(base_url)
info = response.json()

df=pd.DataFrame(None,columns=["Position","Total","Remain"])
i=0;
area = input("請輸入地區:")
for num in info["retVal"]:
    if info["retVal"][num]["sarea"] == area:
        position=(info["retVal"][num]["sna"].split("(")[0])
        total_bike=(int(info["retVal"][num]["tot"]))
        remain_bike=(int(info["retVal"][num]["sbi"]))
        df.loc[i]=[position,total_bike,remain_bike]
        i+=1
print(df)
df.to_csv("adv-10/YouBike_Info.csv")
df.to_excel("adv-10/YouBike_Info.xls")
