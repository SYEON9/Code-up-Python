# ================================#
# 1470: 2차원 배열 지그재그 채우기 2-3
# ================================#
# 입력
n = int(input())

# 배열 채우기
result = []
for i in range(n):
    result.append([])

idx = 1
for i in range(n):       # 2차 리스트
    for j in range(n):   # 1차 리스트
        if i==0:
            result[j].append(idx)
            idx+=1
        elif i%2==0:
            if j == 0:
                idx += 2*n
            result[j].append(idx)
            idx+=1
        elif i%2!=0:
            idx += n-1
            result[j].append(idx)
            idx -= n

# 출력
for i in range(n):
    for j in range(n):
        print(result[i][j], end =' ')
    print()


# 다른 사람 풀이
result = [[0] for i in range(n)]
cnt = 0
for i in range(n):
    if i%2:
        for j in range(n-1, -1, -1):
            cnt += 1
            result[i][j] = cnt
    else:
        for j in range(n):
            cnt += 1
            result[i][j] = cnt

for i in range(n):
    for j in range(n):
        print(result[j][i], end =' ')
    print()

# ================================#
# 1471: 2차원 배열 지그재그 채우기 2-4
# ================================#
# 입력
n = int(input())

# 배열 채우기
n = int(input())
matrix = [[0]*n for i in range(n)]
cnt = 0

for i in range(0, n):
    if not i % 2:
        for j in range(n-1, -1, -1):
            cnt += 1
            matrix[i][j] = cnt
            print(matrix)
    else:
        for j in range(0, n):
            cnt += 1
            matrix[i][j] = cnt

for i in range(0, n):
    for j in range(0, n):
        print(matrix[j][i], end=' ')
    print()
