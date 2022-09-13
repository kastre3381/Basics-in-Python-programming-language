""" STRINGI """

""" formatowanie """

a,b = 1/3,'1/3'
print('a=%f, b=%s'%(a,b))
print('a={:.3f}, b={}'.format(a,b))
print(f'a={a}, b={b}')
print(f'{a=}, {b=}','\n')

""" stringi """

print('abcd efgh'.capitalize())
print('abcd efgh'.title(),'\n')

print('abcdEFGH'.lower())
print('abcdEFGH'.upper())
print('abcdEFGH'.swapcase(),'\n')

print('abcdEFGH'.center(20))
print('abcdEFGH'.center(20,'*'))
print('abcdEFGH'.ljust(20))
print('abcdEFGH'.ljust(20,'*'))
print('abcdEFGH'.rjust(20))
print('abcdEFGH'.rjust(20,'*'),'\n')

print('abcdEFGH'.zfill(20),'\n')
print('   abcdEFGH   '.lstrip()+'*')
print('   abcdEFGH   '.rstrip()+'*')
print('   abcdEFGH   '.strip()+'*','\n')

print('abcd     EFGH'.count(' '))
print('abcd     EFGH'.expandtabs().count(' '),'\n')

s = '56'

print(s.isalnum())
print(s.isalpha())
print(s.isascii())
print(s.isdecimal())
print(s.isdigit())
print(s.isnumeric())
print(s.isidentifier(),'\n')

import keyword

print(keyword.iskeyword(s))
s1='import'
s2='bool'
s3='as'
a=[s1,s2,s3]
for i in a:
    print(i,' : ',keyword.iskeyword(i))
print('\n')

print('abrakadabra'.count('a'))
print('abrakadabra'.startswith('ab'))
print('abrakadabra'.endswith('a'))
print('abrakadabra'.find('a'))
print('abrakadabra'.find('a',4))
print('abrakadabra'.find('z'))
print('abrakadabra'.rfind('a'),'\n')

print('abrakadabra'.index('a'))
# print('abrakadabra'.index('z')) - JEST TO WYJATEK!!!!!!
print('abrakadabra'.index('a',4))
print('abrakadabra'.rindex('a'),'\n')

print('abra kadabra'.split())
print('abra kadabra'.rsplit())
print('abra kadabra'.split('r'))
print('abra kadabra'.rsplit('r'))
print('abra kadabra'.split('r',1))
print('abra kadabra'.rsplit('r',1),'\n')

import re
print(re.split('[rb]','abra kadabra'),'\n')

print('abra\nkadabra'.splitlines())
print('abra kadabra'.partition('br'))
print('abra kadabra'.rpartition('br'),'\n')

print(''.join(('a','b','c')))
print('*'.join(('a','b','c')),'\n')

print('abrakadabra'.replace('a','A'),'\n')

tr=str.maketrans('abc','ABC')
print(tr)
print('abrakadabra'.translate(tr),'\n')

tr=str.maketrans('abc','ABC','r')
print(tr)
print('abrakadabra'.translate(tr),'\n')





