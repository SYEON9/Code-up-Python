# 1368: 평행사변형 출력하기 2
h, k, d= input().split()
h = int(h)
k = int(k)

for i_h in range(h):
    if d == 'L':
        print(' '*i_h, end ='')
        print('*'*k)
    elif d == 'R':
        print(' '*(h-i_h-1), end = '')
        print('*'*k)


# 1369: 빗금 친 사각형 출력하기
n, k = map(int, input().split())
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == 1 or j == n or i ==1 or i==n: 
            print('*', end='')
        elif (i+j-1)%k == 0:
            print('*', end = '')
        else:
            print(' ', end ='')
    print()


# 1370: 지그재그 출력하기
h, r = map(int, input().split())
for i_r in range(r):
    for j1 in range(h):
        print(' '*ji, end ='')
        print('*')
    for j2 in range(h-1, 0, -1):
        print(' '*j2, end ='')
        print('*')
