import random as s
r=int(input("number"))
i= s.randint(1,r)
for a in range(0,r+1):
    print(a)
    if a == i:
        print("yes")
        break