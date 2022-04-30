a=int(input("請輸入年齡"))
b=int(input("你的身分是 1 .是學生 2 .不是學生"))
if a<5:
    print("票價50")
if a>=5:
    if a<=18:
        if b==1:
            print("票價70")
        elif b==2:
            print("票價120")
    elif a>18:
        if b==1:
            print("票價160")
        elif b==2:
            print("票價200")