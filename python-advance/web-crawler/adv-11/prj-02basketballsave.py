import requests, json
import pandas as pd
df=pd.DataFrame(None,columns=["date","home_win","cu_win"])
z=1;
for i in range(1,11):
    base_url="https://tw.global.nba.com/stats2/scores/daily.json?countryCode=TW&gameDate="
    r=str(i)
    d=("2021-11-%s"%i)
    s="&locale=zh_TW&tz=%2B8"
    send_url=base_url
    send_url+=d
    send_url+=s
    
    
    response = requests.get(send_url)
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
    df.loc[z]=[d,home,cu]
    z+=1
    print(df)
    df.to_csv("adv-11/basketball.csv")