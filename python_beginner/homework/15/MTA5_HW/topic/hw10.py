'''
你正在設計一個檔案的函式。如果檔案不存在,
則返回"檔案不存在"。
如果該檔案存在，則該函式返回第一行的內容。
請完成以下程式碼：
import os
def get_file_message(file):
你應該如何安排這些程式碼片段的順序來完成函式?
D A C E B
A.
with open(file, 'r') as file:

B.
return "檔案不存在"

C.
return file.readline()

D.
if os.path.isfile(file):

E.
else:
'''