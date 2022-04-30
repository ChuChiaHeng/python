'''
你正在設計一個python程式去驗證產品編號。
產品編號的格式必須為dd-dddd,並且只包含數字和破折號。
如果格式正確則程式必須列印True,如果格式不正確,則列印False
你要如何完成這段程式碼?請在回答區選擇適當的程式碼片段
__(1)__
parts = ""
__(2)__
    __(3)__
    product_no = input("輸入產品編號(dd-dddd):")
    parts = product_no.split('-')
    if len(parts) == 2:
        if len(parts[0]) == 2 and len(parts[1]) == 4:
            if parts[0].isdigit() and parts[1].isdigit():
            __(4)__
    print(valid)

(B)(1)
A.product_no = ""
B.product_no ="sentinel"
(B)(2)
A.while product_no != "":
B.while product_no != "sentinel":
(A)(3)
A.valid = False
B.valid = True
(B)(4)
A.valid = False
B.valid = True
'''