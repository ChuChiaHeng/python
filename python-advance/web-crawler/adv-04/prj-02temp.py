import requests,json
api_key="589d6c0f8dde4e32241884fd5b5de354"
base_url="http://api.openweathermap.org/data/2.5/weather?"
city_name=input("Entry city name:")
units="metric"
lang="zh_tw"
send_url = base_url
send_url += "appid=" + api_key
send_url += "&q=" + city_name
send_url += "&units=" + units
send_url += "&lang=" + lang
print("%s\n"%send_url)
response=requests.get(send_url)
info=response.json()
if "main" in info.keys():
    temp_info=info["main"]
    current_temperature=temp_info["temp"]
    weather_info=info["weather"][0]
    weather_description=weather_info["description"]
    print("City="+city_name)
    print("Temperature="+str(current_temperature))
    print("Descruption="+str(weather_description))
else:
    print("City Not Found")