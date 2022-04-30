'''
你正設計一個函式用來增加遊戲中的玩家得分。該函式有以下的要求:
1. 如果沒有為變數points指定值, 則points等於1
2. 如果變數plus是True，那麼points必需加倍。
程式碼如下:
01 def add_score(score, plus, points):
02  if plus == True:
03      points = points * 2
04  score = score + points
05  return score
06 points = 5
07 score = 10
08 new_score = add_score(score, True, points)

針對下列每個敘述，如果是正確的就選擇Yes·否則請選擇No。
A。為了符合要求必需將01行更改為以下内容:
    def add_score(score, plus, points = 1):
( )Yes(✅)No

B。一旦使用預設值定義了任何参數,其右側的任何参数也必須使用默認值進行定義。
( )Yes(✅)No

C.如果只用兩個參數呼叫函式, 則第三個参數的值將為None.
( )Yes(✅)No

D。03行的结果會改變在06行中變數points的值·
( )Yes(✅)No
'''