import requests, json
import matplotlib.pyplot as plt
import numpy as np
def createLable(data):
    for item in data:
        height=item.get_height()
        plt.text(
            item.get_x()+item.get_width()/2,
            height,
            str(height),
            ha="center",
        )
base_url="https://tw.global.nba.com/stats2/scores/daily.json?countryCode=TW&gameDate=2021-11-1&locale=zh_TW&tz=%2B8"
response = requests.get(base_url)
info = response.json()
data=info["payload"]["date"]["games"]
home=0
cu=0
for num in range (len(data)):
    home_score=int(data[num]["boxscore"]["homeScore"])
    cu_score=int(data[num]["boxscore"]["awayScore"])
    if home_score>cu_score:
        home+=1
    elif cu_score>home_score:
        cu+=1
print(home)
print(cu)
A=plt.bar("2021-11-1",home,label="主場勝場")
B=plt.bar("2021-11-1",cu,label="客場勝場")
createLable(A)
createLable(B)
plt.legend(loc=1)
plt.show()