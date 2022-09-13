""" LISTY """

import math

""" kopiowanie list """

import copy

k = [1,2,3,4,(5,6,7),[8,9]]
c = copy.copy(k)
c[1]='7,8,9'
print(c,'\n',k,'\n')

d = copy.deepcopy(k)
c[1] = '7,8,9'
print(c,'\n',k,'\n')

""" zliczanie/znajdowanie elementu w liście """

k = [1,2,3,5,(5,6,7),[8,9]]

print(k.count(13))
print(k.count((5,6,7)))
print(k.count(5),'\n')

# print(k.index(13)) - kompilator wypluwa błąd (nie ma 13 w liście)
print(k.index((5,6,7)),'\n')

print(13 in k)
print((5,6,7) in k,'\n')

""" wstawianie elementu do listy """

k = [1,2,3,5,(5,6,7),[8,9]]
k.insert(4,-13)
print(k)
k[1:4] = [7,8,9,10,]
print(k,'\n')

""" usuwanie elementu/ów listy """

k = [1,2,3,5,(5,6,7),[8,9]]
k.remove(1)
print(k)
del k[3]
print(k)
del k[-3:]
print(k)

k = [1,2,3,5,(5,6,7),[8,9]]
print(k.pop(-3))
k.clear()
print(k,'\n')

""" rozbudowywanie listy """

k=[1]*10
k[3]+=1
print(k)
k=[[]]*10
k[3].append(2)
print(k)

k=[[] for i in range(10)]
k[3].append(1)
print(k)
k[3].extend([1,2,3])
print(k,'\n')

""" range function """

k=list(range(10))
print(k)
k=list(range(10,0,-1))
print(k)

for i in k:
    i*=3
    print(i, end=', ')

print('\n')

for i in range(len(k)):
    k[i]*=2
print(k)

for i,v in enumerate(k):
    k[i] = 1 if v>6 else -1
print(k,'\n')


""" lista składana """

k=list(range(10))
for i in range(len(k)):
    k[i]*=3
print(k)
np = [i for i in k if i%2]
print(np)
np = [1 if i>7 else -1 for i in k]
print(np)
k = [(k[i],k[-i-1]) for i in range(len(k)//2)]
print(k,'\n')

""" sortowanie """

k = [(i, float((i+10))//float(i), math.floor(1000*math.sin(float(i+3)))) for i in (range(10,3,-1))]
print(k)
c=k[:]
c.sort()
print(c)

c=k[:]
c.sort(key=lambda x:x[2])
print(c)

c=k[:]
for i in sorted(k):
    print(i)
print(c,'\n')

""" odwrócenie listy """

c=k[:]
c.reverse()
print(c)

c=k[::-1]
print(c)







