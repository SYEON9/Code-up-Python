# 1354: 삼각형 출력하기 2
n = int(input())
for i in range(n, 0, -1):
    print('*'*i)


# 1355: 삼각형 출력하기 3
n = int(input())
for i in range(n, 0, -1):
    con = n-i
    print(' '*con, end = '')
    print('*'*i)


# 1356: 사각형 출력하기 2
n = int(input())
for i in range(n):
    if i==0 or i==n-1: print('*'*n)
    else: 
        print('*', end = '')
        print(' '*n-2, end = '')
        print('*')
