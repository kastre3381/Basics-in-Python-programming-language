import sys 

print('***ZADANIE 1***')

if len(sys.argv)==1:
    print('brak argumentów')
    sys.exit(-1)
else:
    l=list(sys.argv[i] for i in range(1,len(sys.argv)))
    print(l)
    a=''.join(l)
    print(a,'\n')
    
print('***ZADANIE 2***')

listUpper = list(i for i in l if i.isupper())
print(listUpper)

listLower = list(i for i in l if i.islower())
print(listLower)

listDigit = list(i for i in l if i.isdigit())
print(listDigit)

listElse = list(i for i in l if not i.isalnum())
print(listElse,'\n')

print('***ZADANIE 3***')

listLower2 = []

for i in listLower:
    if not i in listLower2:
        listLower2.append(i)
print(listLower2)

listWithNumbers = list((i,listLower.count(i)) for i in listLower2)
print(listWithNumbers)

listWithNumbers.sort(key=lambda x:x[1],reverse=True)
print(listWithNumbers,'\n')
