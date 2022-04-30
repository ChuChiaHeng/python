i=int(input('please input how long is rope?'))
a=0
while i>=20 :
    i/=2
    print(i)
    a+=1
else:
    print('你摺了', a ,'次')