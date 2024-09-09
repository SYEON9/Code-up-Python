# 1272: 기부
# i
money = input().split()
k, h = map(int, input().split())
print(int(money[k-1])+int(money[h-1]))

# ii
k, h = map(int, input().split())
if k%2==0: k = k//2*10
else: k = k//2+1
if h%2==0: h=h//2*10
else: h = h//2+1
print(h+k)



# 1273: 약수 구하기
n = int(input())
for i in range(1,n+1):
    if n%i==0: 
        print(i, end = ' ')


# 1274: 소수 판별
n = int(input())
li = []
for i in range(1, n+1):
    if n%i==0:
        li.append(i)
if len(li)<=2:
    print('prime')
else:
    print('not prime')


# 1275: k 제곱 구하기
n,k = map(int, input().split())
print(n**k)


# 1276: 팩토리얼 계산
n = int(input())
result = 1
for i in range(n, 0, -1):
    result *= i
print(result)


# 1277: 몇 번째 데이터 출력하기
N = int(input())
n = input().split()
middle = len(n)//2
print(n[0], end = ' ')
print(n[middle], end= ' ')
print(n[-1],end = ' ')


# 1278: 자릿수 계산
n = int(input())
s=  str(n)
print(len(s))

# ii
n = int(input())
length = 0
while n>0:
    n//=10
    length += 1
print(length)
