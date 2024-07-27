# 1116: 사칙연산 계산기
a,b = map(int, input().split())
print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={int(a/b)}')


# 1117: 두 실수의 곱
a,b = map(float, input().split())
print(round(a*b, 2))


# 1118: 삼각형의 넓이 구하기
a, b = map(int, input().split())
result = (a*b)/2
print(result)


# 1119: 일을 시간으로 변환
a = int(input())
result = 24*a
print(result)


# 1120: 세 수의 평균
a,b,c = map(int, input().split())
result = (a+b+c)/3
print('%.2f'%result)


# 1121: 나머지 구하기
a,b = map(int, input().split())
result = a%b
print(result)


# 1122: 초를 분/초로 변환
a = int(input())
result1 = a//60
result2 = a%60
print(result1, result2)


# 1123: 섭씨 온도를 화씨 온도로 변환
a = int(input())
k = (9/5)*a + 32
print('%.3f'%k)


# 1125: 8진수 16진수 변환
a = int(input())
print('%o'%a, '%X'%a)

