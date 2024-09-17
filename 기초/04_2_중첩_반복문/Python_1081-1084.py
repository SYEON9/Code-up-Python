# 1081: 주사위를 2개 던지면?
n, m = map(int, input().split())
for i in range(n):
    for j in range(m):
        print(i, end = ' ')
        print(j)


# 1082: 16진수 구구단?
n = int(input(), 16)
for i in range(1, 16):
    print(("%X"%n) + '*' + ("%X"%i) + '=' + ('%X'%(n*i)))


# 1084: 빛 섞어 색 만들기
r,g,b = map(int, input().split())
count = 0
for i in range(r):
    for j in range(g):
        for x in range(b):
            count += 1
            print(i, j, x)
print(count)
