'''
5. 你設計一個Python程式來檢查使用者輸入的數字是1位數、2位數還是2位數以上,
其中規定輸入的值必須是正整數。你要如何完成這段程式碼?

num = int(input("請输入一個正整數: "))
digits = "0"
if num > 0:
    (1)
        digits = "1"
    (2)
        digits = "2"
    (3)
        digits = ">2"
    print(digits + "位數.")
elif num == 0:
    print("輸入值為0")
else:
    print("輸入值並不是正整數")
###############################################
(A)(1) A.if num < 10: B.if num < 100: C.elif num < 100: D.else:
(C)(2) A.if num < 10: B.if num < 100: C.elif num < 100: D.else:
(D)(3) A.if num < 10: B.if num < 100: C.elif num < 100: D.else:
'''