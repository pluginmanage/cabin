# -*- coding: utf-8 -*-
import math
def quadratic(a,b,c):
    x1=(math.sqrt(b*b-4*a*c)-b)/2*a
    x2=(-b-math.sqrt(b*b-4*a*c))/2*a
a=float(input('a为：'))
b=float(input('b为: '))
c=float(input('c: '))
d=b*b-4*a*c
if d>=0:
    r=quadratic(a,b,c)
    print(r)
    else:
        print('error')
