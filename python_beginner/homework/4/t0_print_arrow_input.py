"""
Topic:請使用input輸入要印制的箭頭大小，最小為2行
印出箭頭

e.g.
Please in row: 3
   *
  ***
 *****
   *
   *
   *
"""
n=int(input('please input number'))
for a in range(n):
    print((" "*(n-1))+("*"*(1+a*2)))
    n-=1
n+=a+1
for a in range(n):
    print((" "*(n-1))+("*"*(1)))