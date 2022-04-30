import pandas as pd
import requests, json
import matplotlib.pyplot as plt
from tkinter import*
df=pd.DataFrame(None,columns=["Position","Total","Remain"])
def get_weather ():
    base_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
    response = requests.get(base_url)
    info = response.json()
    city_name=city_info.get()

    
    i=0;
    area = city_name
    for num in info["retVal"]:
        if info["retVal"][num]["sarea"] == area:
            position=(info["retVal"][num]["sna"].split("(")[0])
            total_bike=(int(info["retVal"][num]["tot"]))
            remain_bike=(int(info["retVal"][num]["sbi"]))
            df.loc[i]=[position,total_bike,remain_bike]
            i+=1
    put_city.config(text="儲存成功")
    print(df)
    df.to_csv("adv-10/YouBike_Info.csv")
def s ():
    def createLable(data):
        for item in data:
            height=item.get_height()
            plt.text(
                item.get_x()+item.get_width()/2,
                height,
                str(height),
                ha="center",
            )
    df=pd.read_csv("adv-10/Youbike_Info.csv",encoding="utf8")
    print(df)
    Position=df.loc[:,"Position"]
    Total=df.loc[:,"Total"]
    Remain=df.loc[:,"Remain"]
    A=plt.bar(Position[:8],Total[:8],label="全部停車格")
    B=plt.bar(Position[:8],Remain[:8],label="剩下車輛")
    createLable(A)
    createLable(B)
    plt.legend(loc=1)
    plt.show()
windows=Tk()
windows.title("My gui")

put_haha=Label(windows,text="請輸入行政區")
put_haha.pack()

city_info=Entry(windows)
city_info.pack()

put_city=Label(windows,text="")
put_city.pack()
btn2=Button(windows,text="儲存Youbike資訊",command=get_weather)
btn2.pack()

btn=Button(windows,text="獲取youbike資訊",command=s)
btn.pack()


windows.mainloop()