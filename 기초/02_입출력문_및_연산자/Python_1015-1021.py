# 1015
n = round(float(input()),2)
print(n)


# 1017
n = int(input())
print(n, n, n, end=' ')   # 1
print(f'{n} {n} {n}')     # 2


# 1018
a,b = input().split(':')
print(f'{a}:{b}')


# 1019
# 1
a,b,c = input().split('.')
if len(b)!=2:
    b = '0'+b
if len(c)!=2:
    c = '0'+c
print(f'{a}.{b}.{c}')

# 2
from datetime import datetime

a = input()
result = datetime.strptime(a, '%Y.%m.%d')
print(result)


# 1020
a,b = input().split('-')
print(a+b)


# 1021- 단어 1개 입력받아 그대로 출력하기
# 1
s = input()
print(s)

# 2
s = input()
s = [i for i in s]
result = ''
for i in s:
    result+=i

print(result)
