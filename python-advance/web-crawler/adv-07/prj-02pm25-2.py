import requests, json
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
    for i in range(int(limit)):
        data=info["records"][i]["County"]
        if data== "新北市":
            sitename=(info["records"][i]["SiteName"])
            city=(info["records"][i]["County"])
            aqi=(info["records"][i]["AQI"])
            pm25=(info["records"][i]["PM2.5"])
            status=(info["records"][i]["Status"])
            print("City=%s"%city)
            print("SiteName=%s"%sitename)
            print("AQI=%s"%aqi)
            print("PM2.5=%s"%pm25)
            print("Status=%s"%status)
else:
    print("found error")
