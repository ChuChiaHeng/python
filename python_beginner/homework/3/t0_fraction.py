"""
Topic:輸入分子及分母，確認是否等於 350/450:

Show:Please input numerator"
Input1:70

show:Please input Denominator:
Input2:90
Output:True

Input1:6
Input2:9
Output:False
"""
print("350/450=?")
a=input("Please input numerator.")
b=input("Please input denominator.")
a=int(a)
b=int(b)
if a/b==350/450:
    print("True")
else:
    print("False")