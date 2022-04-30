'''
有一個旅行社需要一個簡單的程式用來輸入合作飯店及民宿的調查資料。
程式必須接受輸入並返回基於五顆星規模的平均評等。
輸出必須四捨五入到小數第二位。你必須完成這個程式碼以符合需求。
你要如何完成這個程式碼?請在回答區選擇適當的程式碼片段。
'''
sum = count = done = 0
average = 0.0
while (done != -1):
    rating = (1)
    if rating == -1:
        break
    sum += rating
    count += 1
average = float(sum / count)
(2) + (3)
'''
(c)(1)   A. print("請輸入評等 (1-5), 完成請輸入-1")
        B. float(input("請输入評等 (1-5), 完成請输入-1"))
        C. input("請输入評等 (1-5), 完成請輸入-1")
        D. input"請輸入評等 (1-5), 完成請输入-1")
(D)(2)   A. output("飯店的平均星级評等是: "
        B. console.input("飯店的平均星级評等是: "
        C. printline("飯店的平均星级評等是: "
        D. print("飯店的平均星级評等是: "
(A)(3)   A. format(average, '.2f'))
        B. format(average, '.2d'))
        C. {average, '.2f'}
        D. format.average.{2d}
'''