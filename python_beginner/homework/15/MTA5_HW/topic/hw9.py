'''
你必須開發一個簡單的Python程式來執行以下動作:
1. 檢查檔案是否存在。
2. 如果該檔案存在,就顯示檔案內容。
3. 如果該檔案不存在,就使用指定的名稱新增檔案。
4. 在檔案最後加入文字:"這是檔案結尾"。
你需要完成程式碼以符合要求。
你要如何完成這段程式碼?
請在回答區選擇適當的程式碼片段。

import os
if __(1)__:
    file = open('theFile.txt')
    __(2)__
    file.close()
file = __(3)__
__(4)__("這是檔案結尾")
file.close()

(D)(1)
A. isfile('theFile.txt')
B. os.exist('theFile.txt')
C. os.find('theFile.txt')
D. os.path.isfile('theFile.txt')
(B)(2)
A. output('theFile.txt')
B. print(file.get('theFile.txt'))
C. print(file.read())
D. print('theFile.txt')
(C)(3)
A. open('theFile.txt', 'a')
B. open('theFile.txt', 'a+')
C. open('theFile.txt', 'w')
D. open('theFile.txt', 'w+')
(C)(4)
A. Append
B. file.add
C. file.write
D. write
'''