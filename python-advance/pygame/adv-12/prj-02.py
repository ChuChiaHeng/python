data = {
    "Name": "Singular",
    "Score": [{
        "Math": 100,
        "English": 99
    }, {
        "Chinese": 98,
        "Nature": 97
    }]
}
print(data["Name"])
print(data["Score"][0]["Math"])
print(data["Score"][1]["Chinese"])