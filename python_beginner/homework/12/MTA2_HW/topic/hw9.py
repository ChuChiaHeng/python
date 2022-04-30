'''
你正在設計一個電子商務程式,它可以接受來自使用者输入,
並以逗分隔的格式輸出資料。你可以編寫下程式碼接受資料輸入:
'''
product = input("輸入産品名稱:")
qty = input("輸入數量:")
'''
輸出必須符合以下要求:
1. 字串必須括在雙引號內。
2. 數字不得用引號或其他字元括起來。
3. 每個產品必須用逗號隔開。
你需要完成程式碼以符合要求。你應該使用哪三個程式碼片段?
( )A. print('"{0}",{1}'.format(product, qty))
( )B. print('"' + product + '",' + qty)
( ✔)C. print('"%s",%s' % (product, qty))
( )D. print("{0},{1}".format(product, qty))
( )E. print(product + ',' + qty)
'''