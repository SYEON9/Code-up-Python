# =======================================#
# 1467: 2차원 배열 순서대로 채우기 1-8
# =======================================#
# 입력
n,m = map(int, input().split())

# 배열 채우기
inp = n*m
result = []
for i in range(n):
    result.insert(0, [])
    for j in range(m):
        result[0].append(inp-n*j)
    inp = inp - 1

# 출력
for i in range(n):
    for j in range(m):
        print(result[i][j], end = ' ')
    print()
