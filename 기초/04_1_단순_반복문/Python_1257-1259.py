# 1257: 두 수 사이의 홀수 출력하기
start, end = map(int, input().split())
for i in range(start, end+1):
    if i%2!=0: print(i, end=' ')


# 1258: 1부터 n까지 합 구하기
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)


# 1259: 1부터 n까지 중 짝수의 합 구하기
n = int(input())
sum = 0
for i in range(1, n+1):
    if i%2==0: sum += i
print(sum)
