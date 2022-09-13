""" zadania """
import math 

k=list(range(1,50,3))
print(k)

for i in range(len(k)-1,0,-1):
    if k[i]%4==3:
        del k[i]
print(k)

i=len(k)-1

while i>-1:
    if k[i]%2==1:
        del k[i]
    i-=1
print(k)

for i in range(1,len(k),2):
    print(k[i], end=', ')
print('\n')

s = [(i,k[i]) for i in range(len(k))]
print(s)

s.reverse()
print(s)

s.sort(key=lambda x:x[1])
print(s)

y = [i for i in range(1,30,3)]
print(y)

l = [(i,y[i]) for i in range(len(y)) if y[i]%2==0]
print(l)

w = [math.sin(i) for i in range(10)]
print(w)

k=[w[0]]
print(k)
j=0
for i in range(1,len(w)):
    if w[i]>k[j]:
        k.insert(i, w[i])
        j+=1
print(k)




