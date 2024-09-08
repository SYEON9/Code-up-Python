# 1266: n개의 수의 합
n = int(input())
num = input().split()
sum = 0
for i in range(n):
    sum += int(num[i])
print(sum)


# 1267: n개의 수 중 5의 배수의 합
n = int(input())
num = input().split()
sum = 0
for i in range(n):
    if int(num[i])%5 == 0:
        sum += int(num[i])
print(sum)


# 1268: n개의 수 중 홀수의 개수
n = int(input())
num = input().split()
count = 0
for i in range(n):
    if int(num[i])%2!=0:
        count += 1
print(count)


# 1269: 수열의 값 구하기
a, b, c, n = map(int, input().split())
for i in range(n-1):
    a = a*b+c
print(a)


# 1270: 1의 개수는? 1
n = int(input())
count = 0
for i in range(1, n+1):
    if i%10 == 1: count += 1
print(count)


# 1271: 최댓값 구하기
n = int(input())
num = input().split()
num.sort()
print(num[-1])
