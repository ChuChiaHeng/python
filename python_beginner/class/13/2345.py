import datetime
next = datetime.datetime.strptime('1/6/2022','%m/%d/%Y').date()
print(type(next))
now = datetime.date.today()
print(type(next))
diff=next-now
print(diff)