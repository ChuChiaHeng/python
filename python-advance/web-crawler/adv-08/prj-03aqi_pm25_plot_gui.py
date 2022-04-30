import requests, json
import matplotlib.pyplot as plt
import numpy as np
from tkinter import*
def get_weather ():
    city_name=city_info.get()
    base_url="https://data.epa.gov.tw/api/v1/"
    api_num="aqx_p_432?"
    offset="0"
    limit="50"
    api_key="24252b6d-44dc-43b0-98cd-e6ef79d3d1cf"
    send_url=base_url
    send_url+=api_num
    send_url+=("offset="+offset)
    send_url+=("&limit="+limit)
    send_url+=("&api_key="+api_key)
#print(send_url)
    response=requests.get(send_url)
    info=json.loads(response.text)
    city_name=city_info.get()
    if "fields" in info.keys():
        aqi_value=[]
        aqi_posit=[]
        aqi_pm25=[]
        
        for i in range(int(limit)):
            data=info["records"][i]["County"]
            
            if data== city_name:
                aqi_posit.append(info["records"][i]["SiteName"])
                aqi_value.append(int(info["records"][i]["AQI"]))
                aqi_pm25.append(int(info["records"][i]["PM2.5"]))
        show=""
        for i in range(len(aqi_value)):
            show+=("SiteName=%s,AQI=%d,PM2.5=%d\n"%(aqi_posit[i],aqi_value[i],aqi_pm25[i]))
        put_city.config(text=show)
   
            
                    
        plt.plot(aqi_posit,aqi_value,"r-.",label="AQI")
        plt.plot(aqi_posit,aqi_pm25,"g--",label="PM2.5")        
        plt.legend(loc=7)
        plt.show()
    else:
        print("found error")
        




windows=Tk()
windows.title("My Weather")
put_haha=Label(windows,text="請輸入城市")
put_haha.pack()

city_info=Entry(windows)
city_info.pack()
put_city=Label(windows,text="")
put_city.pack()
btn=Button(windows,text='獲取城市空氣品質',command=get_weather)
btn.pack()
windows.mainloop()