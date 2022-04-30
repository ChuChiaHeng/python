import requests, json
import matplotlib.pyplot as plt
import numpy as np
from tkinter import*

def get_weather ():
    base_url="https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
    response=requests.get(base_url)
    info=json.loads(response.text)
    city_name=city_info.get()
    ggg=[]
    hhh=[]
    ttt=[]
    yyy=[]

    for i in range(1,len(info["retVal"])):
        num=("%04d"%i)

        if num in info["retVal"].keys() and info["retVal"][num]["sarea"]==city_name:
            ggg.append(info["retVal"][num]["sarea"])
            hhh.append(info["retVal"][num]["sna"].split("(")[0])
            ttt.append(int(info["retVal"][num]["tot"]))
            yyy.append(int(info["retVal"][num]["sbi"]))
    show=""
    for j in range(len(hhh)):
        show+=("行政區:%s,地點:%s,總共車輛:%d,剩餘車輛:%d\n" % (ggg[j],hhh[j],ttt[j],yyy[j]))
    #print(show)
    put_city.config(text=show)


    plt.plot(hhh,ttt,"r-.",label="總共車輛")
    plt.plot(hhh,yyy,"g--",label="剩餘車輛")        
    plt.legend(loc=7)
    plt.show()

def clear ():
    put_city.config(text="")

windows=Tk()
windows.title("My gui")

put_haha=Label(windows,text="請輸入行政區")
put_haha.pack()

city_info=Entry(windows)
city_info.pack()

put_city=Label(windows,text="")
put_city.pack()

btn=Button(windows,text="獲取youbike資訊",command=get_weather)
btn.pack()

btn2=Button(windows,text="清除",command=clear)
btn2.pack()
windows.mainloop()