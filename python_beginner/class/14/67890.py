import random
a=int(input("輸入密碼1~1000000"))
s=0
while True:
    w=random.randint(1,1000001)
    if w!=a:
        print(w)
        s+=1
        continue
    if w==a:
        break
print("破解密碼，密碼是%d"%w)
print("找了%d"%s+"次")
