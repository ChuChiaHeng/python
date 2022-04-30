from tkinter import*
import requests,json
api_key="589d6c0f8dde4e32241884fd5b5de354"
base_url="http://api.openweathermap.org/data/2.5/weather?"
units="metric"
lang="zh_tw"
def get_weather():
    city_name=city_info.get()
    send_url = base_url
    send_url += "appid=" + api_key
    send_url += "&q=" + city_name
    send_url += "&units=" + units
    send_url += "&lang=" + lang
    print("%s\n"%send_url)
    response=requests.get(send_url)
    info=response.json()
    print(info)
    if "main" in info.keys():
        temp=info["main"]["temp"]
        desc=info["weather"][0]["description"]

        put_city.config(text="City="+city_name)
        put_temp.config(text="Temperature="+str(temp))
        put_disc.config(text="Description="+str(desc))
    else:
        put_city.config(text="City Not Found")
windows=Tk()
windows.title("My Weather")
put_city=Label(windows,text="")
put_city.pack()
put_temp=Label(windows,text="")
put_temp.pack()
put_disc=Label(windows,text="")
put_disc.pack()
city_info=Entry(windows, text="")
city_info.pack()
btn=Button(windows,text='獲取現在天氣',command=get_weather)
btn.pack()
windows.mainloop()