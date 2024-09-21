# 1365: 사각형 출력하기 3
n = int(input())
# 첫번째 줄
print('*'*n)
# 중간영역1
for i in range(1, int(n/2)):
    for j in range(n):
        if j==0 or j==i or j==n-1 or j == n-i-1:
            print('*', end ='')
        else:
            print(' ', end ='')
    print()
# 중간영역2
if n%2!=0: 
    for i in range(n):
        if i==0 or i==n-1 or i==int(n/2):
            print('*', end='')
        else: print(' ', end ='')
    print()
else:
    for i in range(int(n/2)-1, int(n/2)):
        for j in range(n):
            if j==0 or j==i or j==n-1 or j == n-i-1:
                print('*', end ='')
            else:
                print(' ', end ='')
    print()
# # 중간영역3
for i in range(int(n/2)+1, n-1):
    for j in range(n):
        if j==0 or j==i or j==n-1 or j == n-i-1:
            print('*', end ='')
        else:
            print(' ', end ='')
    print()
# 마지막 줄
print('*'*n)


# 1366: 사각형 출력하기 4
n = int(input())
# 첫번째 줄
print('*'*n)
# 중간영역1
for i in range(1, int(n/2)):
    for j in range(n):
        if j==0 or j==i or j==n-1 or j == n-i-1 or j==int(n/2):
            print('*', end ='')
        else:
            print(' ', end ='')
    print()
# 중간영역2
print('*'*n)
# # 중간영역3
for i in range(int(n/2)+1, n-1):
    for j in range(n):
        if j==0 or j==i or j==n-1 or j == n-i-1 or j==int(n/2):
            print('*', end ='')
        else:
            print(' ', end ='')
    print()
# 마지막 줄
print('*'*n)


# 1367: 평행사변형 출력하기 1
n = int(input())
for i in range(1, n+1):
    print(' '*(n-i), end = '')
    print('*'*n)
# ii
n = int(input())
for x in range(n + n - 1, n-1, -1):
    for y in range(x - n):
        print(" ", end="")
    for y in range(n):
        print("*", end="")
    print()
