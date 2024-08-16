# 1201: 정수판별
n = int(input())
print('양수' if n%2==0 else (0 if n==0 else '음수'))


# 1202: 등급판정
n = int(input())
if n>=90: print('A')
elif n>=80: print('B')
elif n>=70: print('C')
elif n>=60: print('D')
else: print('F')


# 1203: 비만도 측정 0
n = int(input())
if n<=10: print('정상')
elif n>10 and n<=20: print('과체중')
else: print('비만')


# 1204: 영어 서수로 표현하기
n = int(input())
if n==1: print('1st')
elif n==2: print('2nd')
elif n==3: print('3rd')
else: print(n,'th', sep='')


# 1205: 최댓값
a,b = map(int, input().split())
plus = abs(a+b)
minus = abs(a-b)
mul = a*b
div1 = a/b
div2 = b/a
result = [plus, minus, mul, div1, div2]
print(sorted(result, reverse=True)[0])


# 1206: 배수
a,b = map(int, input().split())
if b%a==0: print(f'{a}*{int(b/a)}={b}')
elif a%b==0: print(f'{b}*{int(a/b)}={a}')
else: print('none')
