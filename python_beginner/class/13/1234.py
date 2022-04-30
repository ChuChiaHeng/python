import datetime
day=(input("What is your birthday?"))
print(day)
birth=datetime.datetime.strptime(day,"%m/%d/%Y")
print(birth.date())