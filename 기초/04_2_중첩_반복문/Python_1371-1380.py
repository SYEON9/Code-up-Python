## 1371: 마름모 출력하기
n = int(input())

for i in range(n):
    for j in range(n-i-1, 0,-1):
        print(' ', end ='')
    print('*', end ='')
    for j in range(i*2):
        print(' ', end ='')
    print('*')

for i in range(n):
    for j in range(i):
        print(' ', end ='')
    print('*', end ='')
    for j in range((n-i-1)*2, 0, -1):
        print(' ', end ='')
    print('*')


# 1378: 수열의 합
n = int(input())
su = 0
li = []
for i in range(1, n+1):
    su += i
    li.append(su)
print(sum(li))


# 1380: 두 주사위의 합
n = int(input())
for i in range(1,7):
    for j in range(1, 7):
        if i+j == n: 
            print(i, end =' ')
            print(j)
