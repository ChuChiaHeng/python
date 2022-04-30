'''
你設計一個讀取檔案後將檔案中的每一行列印出來的函式。程式碼如下:
01 def print_file(filename):
02  line = None
03  if os.path.isfile(filename):
04      data = open(filename, 'r')
05      for line in data:
06          print(line)
當你執行該程式時,你會收到03行上的錯。導致錯誤的原因是什麼?
(✅)A. 你需要導入os模組
()B. path方法並不存在os模组中。
()C. path物件中不存在isfile方法。
()D. isfile 方法不接受一個參数
'''