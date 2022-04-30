'''
你設計了一個函式來執行除法,因為除法的除數不能為零,
所以在函式中必須要針對這個重點進檢查。
你要如何完成這段程式碼?
請在回答區擇適當的程式碼片段。
def safe_divide(numerator, denominator):
    __(1)__
        print("你少填了被除或除数")
    __(2)__
        print("除数為零會産生錯誤")
    else:
        return numerator / denominator
(A)(1)
A. if numerator is None or denominator is None:
B. if numerator is None and denominator is None:
C. if numerator = None or denominator = None:
D. if numerator = None and denominator = None:
(B)(2)
A. elif denominator == O:
B. elif denominator = 0:
C. elif denominator != 0:
D. elif denominator in 0:
'''