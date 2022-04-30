'''
顯示今天的日期，
零食的保存期限為2/21/2022，
請顯示還有多久會到保存期限。
'''
import datetime
next = datetime.datetime.strptime('2/21/2022','%m/%d/%Y').date()
now = datetime.date.today()
diff=next-now
print("零食有效日期剩"+str(diff))