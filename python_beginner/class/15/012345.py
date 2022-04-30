import math
def calculate_val(value):
    aa=math.floor(value)
    if (value-aa)>0.4:
        new=value=math.ceil(value)
    else:
        new=value=math.floor(value)
    return new
a=calculate_val(-45.12)
print(a)
b=calculate_val(30.6)
print(b)
c=calculate_val(50.4)
print(c)
def calculate_add(val1,val2,val3):
    return val1+val2+val3
print(calculate_add(a,b,c))