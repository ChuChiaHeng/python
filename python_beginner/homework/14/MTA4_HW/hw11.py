'''
6. 你在設計一個Python程式遊戲,讓參加的人從1到100間猜一個數字，
最多有三次機會。程式碼如下:
01 from random import randint
02 target = randint(1,100)
03 chance = 1
04 print("猜一個從1到100的整数。你將有3機會.")
05
06  guess=int(input("請输入一個整數:")
07  if guess > target:
08      print("數字太大了,低一點")
09  elif guess < target:
10      print("數字太小了,猜高一點")
11  else:
12      print("精對了!")
13
14

請將正確的程式碼片段填入A、B、C選項中：
while chance <= 3:
while chance < 3:
break
pass
chance += 1
while chance < 3
chance = 2
A.在05行你要使用哪個程式碼片段?while chance <= 3:
B.在13行你要使用哪個程式碼片段?break
C.在14行你要使用哪個程式碼片段?chance += 1

'''