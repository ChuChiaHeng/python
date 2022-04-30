"""
Topic:輸入三角形三邊，判斷是否能構成三角形，
　　　是三角形則顯示面積和周長，不行則顯示，無法構成三角形:
Triangle Area formula:
p = 1/2 (a+b+c)
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

e.g.
Show:a ="
Input1:3

Show:b ="
Input2:4

Show:c ="
Input3:5

output:
perimeter: 12.000000
Area: 6.000000
"""
a=input("a=?")
b=input("b=?")
c=input("c=?")
a=int(a)
b=int(b)
c=int(c)
p =1/2*(a+b+c)
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
if c<a+b and b<a+c and a<b+c:
    print(a+b+c)
    print(area)
else:
    print("can't make a triangle")