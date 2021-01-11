import numpy as np
import math
from math import sqrt

y=int(input('Введите значение y: '))
a=int(input('Введите значение a: '))
p=int(input('Введите значение p: '))

for i in range(0,round(sqrt(p))+1):
    if i*i>p:
        k=i
        m=i
        print("m =", m, ", k =", k)
        break
    if i*(i+1)>p:
        k=i
        m=i+1
        print("m =", m, ", k =", k)
        break

print ("")

print ("Шаг младенца: ")
x1=np.zeros(m)
for i in range(0,m):
    x1[i]=(y*(a**i))%p
print(x1)

print ("")

print ("Шаг великана: ")
x2=np.zeros(k)
for i in range(1,k):
    x2[i-1]=(a**(m*i))%p
print(x2)

for k1 in range(0,m):
    for k2 in range(0,k):
        if (x1[k1]==x2[k2]):
            i=k2+1
            j=k1
            break
        
print ("")
        
x=i*m - j
print("x =",x)
