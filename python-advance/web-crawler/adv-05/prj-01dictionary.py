data = {
    "coord": {
        "lon": 121.5319,
        "lat": 25.0478
    },
    "weather": [
        {
            "status": "Clouds"
        },
        {   
            "des": "多雲"
        }               
    ],
    "temperature": [
        {   
            "temp": 32.47,
            "temp_min": 30.6,
            "temp_max": 33.93
        }
    ],
    "name": "Taipei",
} 
key=input("find the key:")
if key in data.keys():
    if key == "coord":
        print("lon=%s"%data[key]["lon"])
        print("lat=%s"%data[key]["lat"])
    elif key == "weather":
        print("status=%s"%data[key][0])
        print("des=%s"%data[key][1])
    elif key == "temperature":
        print("temp=%s"%data[key][0]["temp"])
        print("temp_min=%s"%data[key][0]["temp_min"])
        print("temp_max=%s"%data[key][0]["temp_max"])
    elif key=="name":
        print("name=%s"%data[key])
else:
    print("沒東西")