'''
你設計了一個程式要依學生的成績來顯示等級,它的規定如下:
分數    等級
100到90 甲等
89到80  乙等
79到70  丙等
69到60  丁等
60以下  不及格
例如,如果使用者輸入90,則輸出應該是,你的成績為甲等"相同的,
如果使用者輸入 89,則出該為你的成績為乙等”你要如何完成這段程式碼?
請在回答區選擇適當的程式碼片段。
'''
#宇母等级轉换器
grade=int(input("請输入數字等级")
__(1)__
    letter_grade = '甲等'
__(2)__
    letter_grade = '乙等'
__(3)__
    letter_grade = '丙等'
__(4)__
    letter_grade = '丁等'
else:
    letter_grade = '不格'
print("你的成绩為 :", letter_grade)
'''
(B)(1)
A. if grade <= 90:
B. if grade >= 90:
C. elif grade > 90:
D. elif grade >= 90:
(D)(2)
A. if grade > 80:
B. if grade >= 80:
C. elif grade > 80:
D. elif grade >= 80:
(D)(3)
A. if grade > 70:
B. if grade >= 70:
C. elif grade > 70:
D. elif grade >= 70:
(D)(4)
A. if grade > 60:
B. if grade >= 60:
C. elif grade > 60:
D. elif grade >= 60:

'''