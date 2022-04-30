"""
輸入一數字n為尋找的區間範圍, 找出區間範圍
的質數顯示在螢幕上，其餘不顯示。


"""
n=int(input("number:"))
if n>1:
    for a in range(2,n+1):
        for s in range(2,a):
            if a%s==0 :
                break
        else:
            print(a)
else:
    print('error')