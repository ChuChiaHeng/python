a=float(input("請輸入體溫"))
b=int(input("你有沒有戴口罩 1 .有 2 .沒有"))
if a>=37.5:
    if a<38:
        if b==1:
            print("請戴好口罩，保持社交距離，才可施打疫苗。")
        elif b==2:
            print("請離場")
    elif a>=38:
        print("立刻就醫")
elif a>=38:
    print("立刻就醫")
elif a<=34:
    print("立刻就醫")
else:
    if b==1:
        print("可施打疫苗")
    elif b==2:
        print("請將口罩戴上")