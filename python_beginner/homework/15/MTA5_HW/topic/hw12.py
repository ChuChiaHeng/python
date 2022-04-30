'''
你正在設計一個Python程式來讀取學生資料的檔案，
文件中包含學生的班級、座號和姓名，下面顯示的是檔案中的資料範例:
'1A', 1, 'David'
'1A', 2, 'Mary'
程式碼必須符合以下的需求:
1. 檔案的每一行都必須讀取和列印。
2. 如果遇到空行,則必須忽略。
3. 在完成所有行的讀取後,必須關閉檔案。
你創建了以下的程式碼。其中包含的行號只是做為參考。

01 students = open("students.txt", 'r')
02 eof = False
03 while eof == False:
04  line = students.readline()
05
06
07      print(line.strip())
08  else:
09      print("檔業結束")
10      eof = True
11 students.close()

在05及06行你應該編寫哪些程式碼?
( )A.
05 if line != "":
06 if line != "\n":
( )B.
05 if line != '\n':
06 if line != "":
(✅)C.
05 if line != "\n":
06 if line != None:
( )D.
05 if line != "":
06 if line != "":
'''