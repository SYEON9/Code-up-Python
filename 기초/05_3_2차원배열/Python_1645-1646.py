# ====================================# 
# 1645: 2차원 배열 순서대로 채우기 1-6
# ====================================# 
# 입력
n, m = map(int, input().split())

# 배열 채우기
result = []
inp = n*m
for i in range(n):
    result.append([])
    for j in range(m):
        result[i].insert(0, inp)
        inp -= 1

# 출력
for i in range(n):
    for j in range(m):
        print(result[i][j], end = ' ')
    print()


# ====================================# 
# 1646: 2차원 배열 순서대로 채우기 1-7
# ====================================# 
# 입력
n, m = map(int, input().split())

# 배열 채우기
result = []
inp = n*m
# i: 방법 1
for i in range(n):
    result.append([])
for j in range(m):
    for i in range(n):
        result[i].append(inp)
        inp -= 1

# 방법2
for i in range(n):
    result.append([])
    for j in range(m):
        result[i].append(inp)
        inp = inp-n
    inp = n*m - (i+1)

# 출력
for i in range(n):
    for j in range(m):
        print(result[i][j], end = ' ')
    print()
       
