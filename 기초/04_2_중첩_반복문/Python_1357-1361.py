# 1357: 삼격형 출력하기 4
n = int(input())
cou = 0
for i in range(1, n+1):
    print('*'*i)
for i in range(n-1, 0, -1):
    print('*'*i)


# 1358: 삼각형 출력하기 5
#i
n = int(input())
con = 0
for i in range(1, n+1, 1):
    if i%2!=0:
        print((n//2-con)*'*', end = '')
        print(i*'*', end = '')
        print((n//2-con)*'*')
        con += 1

# ii
# 1358: 삼각형 출력하기 5
n = int(input())
for i in range(1, n+1, 2):
    print(((n-i)//2)*' ', end = '')
    print(i*'*')
    con += 1


# 1361: 별 계단 만들기
n = int(input())
for i in range(n):
    print(' '*i, end = '')
    print('*'*2)
