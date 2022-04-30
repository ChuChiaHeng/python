import requests, json
import matplotlib.pyplot as plt
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
if "fields" in info.keys():
    aqi_value=[]
    aqi_posit=[]
    aqi_pm25=[]
    for i in range(int(limit)):
        data=info["records"][i]["County"]
        if data== "新北市":
            aqi_posit.append(info["records"][i]["SiteName"])
            aqi_value.append(info["records"][i]["AQI"])
            aqi_pm25.append(info["records"][i]["PM2.5"])
    plt.plot(aqi_posit,aqi_value,"r-o",label="AQI")
    plt.plot(aqi_posit,aqi_pm25,"g--",label="PM2.5")        
    plt.legend(loc="upper left")
    plt.show()
else:
    print("found error")
