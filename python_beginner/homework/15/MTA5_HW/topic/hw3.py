'''
你要設計一款以使用者年齡進行電影分級的程式。這個函式必須符合以下要求:

1. 任何18歲或以上的人會顯示"限制級"的訊息
2. 任何13歲或以上,但小於18歲的人都會顯示"輔導級"的訊息
3. 任何12歲或更年輕的人都會顯示"普通級"的訊息
4. 如果年齡未知,則會顯示"未知"的訊息
你需要完成程式碼以符合要求,應該要如何完成這段程式碼?
請在回答區選擇適當的程式碼片段。
def get_rating(age):
    rating = ""
    if (1)
    elif (2)
    elif (3)
    else (4)
    return rating

(B)(1)   A. age<13:rating="普通級" B. age<18:rating="輔導级"
        C. :rating="限制" D. age==None:rating="未知"
(A)(2)   A. age<13:rating="普通级" B. age<18:rating="輔導級"
        C. :rating="限制级" D. age==None:rating-"未知"
(D)(3)   A. age<13:rating="普通級" B. age<18:rating="輔導极"
        C. :rating="限制級" D. age=-None:rating="未知"
(C)(4)   A. age<13:rating="普通級" B.age<18:rating="輔導级"
        C. :rating="限制級" D. age==None:rating="未知"
'''