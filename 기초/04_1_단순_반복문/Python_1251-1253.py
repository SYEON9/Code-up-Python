# 1251: 1부터 100까지 출력하기
for i in range(1, 101):
    print(i, end=' ')


# 1252: 1부터 n까지 출력하기
n = int(input())
for i in range(1, n+1):
    print(i, end = ' ')


# 1253: a부터 b까지 출력하기
a,b = map(int, input().split())
for i in range(a, b+1):
    print(i, end=' ')
