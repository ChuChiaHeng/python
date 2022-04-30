'''
17.租車公司需要一種方法來決定客戶租用車輛的費用。
該費用取決於車輛歸還的時間。
然而,週四和週日也有特別的費率。費用結構如下所示:
1. 費用是每天100美元。
2. 如果車輛在晚上 11點後返還,客戶將被多收取額外一天的費用。
3. 如果車輛是在星期天租的,客户可享受 10%的折扣。
4. 如果車輛是在星期四租的,客戶可以享受 20%的折扣。
你需要撰寫程式碼去符合這個需求,要如何完成這段程式碼?
'''
#車輛出租計算機
ontime= input("車子是在晚上11點前返還的嗎? y 或 n").lower()
days_rented = int(input("車子出租了幾天?"))
day_rented = input("車子是在星期幾出租?").capitalize()
cost_per_day = 100
if ontime __(1)__:
    days_rented += 1
if day_rented __(2)__:
    total = (days_rented * cost_per_day) * 0.9
elif day_rented __(3)__:
    total = (days_rented * cost_per_day) * 0.8
else:
    total = days_rented * cost_per_day
print("車辆的租借費用為: $",total)
'''
(B)(1)A.!="n": B. =="n": C. =="y":
(A)(2)A.=="Sunday ": B.>="Sunday ": C. is " Sunday ":
(A)(3)A.=="Thursday": B.<="Thursday": C. is "Thursday":
'''