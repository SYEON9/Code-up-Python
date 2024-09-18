# 1351: 구구단 출력하기2
start, end = map(int, input().split())
for i in range(start, end+1):
    for j in range(1, 10):
        print(f'{i}*{j}={i*j}')


# 1352: 사각형 출력하기 1
n = int(input())
for i in range(n):
    print('*'*n)


# 1353: 삼각형 출력하기 1
n = int(input())
for i in range(1,n+1):
    print('*'*i)
