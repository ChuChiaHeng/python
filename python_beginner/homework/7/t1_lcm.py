'''
使用者輸入兩個數num1 and num2，
並使用function def 求最小公倍數
value = lcm(num1, num2)
'''
def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
num1 = int(input("num1: "))
num2 = int(input("num2: "))
print(lcm(num1, num2))