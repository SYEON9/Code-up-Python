# 1460: 2차원 배열 순서대로 채우기 1-1
# 입력
n = int(input())

# 배열 채우기
result = []
out = 1
for i in range(n):
    result.append([])
    for j in range(n):
        result[i].append(out)
        out += 1

# 출력
for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')
    print()

# !!출력만 같게 하는 경우!!
n = int(input())
for i in range(n):
    for j in range(1, n+1):
        print(n*i+j, end = ' ')
    print()



# 1461: 2차원 배열 순서대로 채우기 1-2
# 입력
n = int(input())

# 배열 채우기 
result = []
out = 1
for i in range(n):
    result.append([])
    for j in range(n):
        result[i].insert(0, out)
        out += 1

# 출력
for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')
    print()
