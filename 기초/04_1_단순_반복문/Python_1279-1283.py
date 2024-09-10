# 1279: 홀수는 더하고 짝수는 빼고 1
a, b = map(int, input().split())
result = 0
for i in range(a, b+1):
    if i%2==0: result -= i
    else: result += i
print(result)


# 1280: 홀수는 더하고 짝수는 빼고 2
a, b = map(int, input().split())
result = 0
for i in range(a, b+1):
    if i%2==0: 
        print(f'-{i}', end='')
        result -= i
    else:
        print(f'+{i}', end='')
        result += i
print(f'={result}')


# 1281: 홀수는 더하고 짝수는 빼고 3
a, b = map(int, input().split())
result = 0
for i in range(a, b+1):
    if i%2==0: 
        print(f'-{i}', end='')
        result -= i
    else:
        if i==a: 
            print(i, end = '')
            result += i
        else:
            print(f'+{i}', end='')
            result += i
print(f'={result}')


# 1282: 제곱수 만들기
# ----------------------------------------------#
# i : 메모리 초과
# >> '**'보다 '*' 가 메모리를 적게 사용함. 
# np.sqrt()가 많은 메모리를 차지함. 
# ----------------------------------------------# 
import numpy as np

n = int(input())
num = 1
while num**2 < n:
    num += 1
s = (num-1)**2    # n보다 작은 제곱수 중 가장 큰 값
k = n-s
t = np.sqrt(s)
print(f'{k} {t}')

# ----------------------------------------------# 
# ii : for문, if 문을 사용하여 메모리 사용량을 줄임. 
# ----------------------------------------------# 
n = int(input())
for i in range(1, n+1):
    t = i*i
    if t>n:
        k = (i-1)*(i-1)
        k = n-k
        t = i-1
        break
print(k, t)


# 1283: 주식 투자
a = int(input())
money = a
b = int(input())
di = input().split()

for i in range(len(di)):
    money = money+money*(int(di[i])/100)
result = round(money-a)

print(result)
if result>0: print('good')
elif result == 0: print('same')
else: print('bad')
