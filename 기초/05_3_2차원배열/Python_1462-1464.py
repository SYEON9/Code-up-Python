# ==============================================# 
# 1462: 2차원 배열 순서대로 채우기 1-3
# ==============================================# 
# 입력
n = int(input())

# 배열 채우기
result = []
plus = 1
for i in range(n):
    result.append([])
    for j in range(n):
        result[i].append(plus+j*n)
    plus += 1

# 출력
for i in range(n):
    for j in range(n):
        print(result[i][j], end = ' ')
    print()


# ==============================================# 
# 1463: 2차원 배열 순서대로 채우기 1-4
# ==============================================# 
# 입력
n = int(input())

# 배열 채우기
m = n
result = []
for i in range(n):
    result.append([])
    for j in range(n):
        result[i].append(m+j*n)
    m -= 1

# 출력
for i in range(n):
    for j in range(n):
        print(result[i][j], end =' ')
    print()



# ==============================================# 
# 1464: 2차원 배열 순서대로 채우기 1-5
# ==============================================# 
# 입력
n, m = map(int, input().split())

# 배열 채우기
result = []
k = n*m
for i in range(n):
    result.append([])
    for j in range(m):
        result[i].append(k-j)
    k = k - m

# 출력
for i in range(n):
    for j in range(m):
        print(result[i][j], end=' ')
    print()


