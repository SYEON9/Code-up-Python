# =================================#
# 1468: 2차원 배열 지그재그 채우기 2-1
# =================================#
# 입력
n = int(input())

# 배열 지그재그 채우기
result = []
for i in range(1, n+1):
    result.append([])
    for j in range(1, n+1):
        if i %2 == 1:
            result[i-1].append(j + n*(i-1))
        elif i%2==0:
            result[i-1].insert(0, j+n*(i-1))

# 출력
for i in range(n):
    for j in range(n):
        print(result[i][j], end =' ')
    print()



# =================================#
# 1469: 2차원 배열 지그재그 채우기 2-2
# =================================#
# 입력 
n = int(input())

# 배열 지그재그 채우기
result = []
for i in range(1, n+1):
    result.append([])
    for j in range(1, n+1):
        if i %2 == 0:
            result[i-1].append(j + n*(i-1))
        elif i%2==1:
            result[i-1].insert(0, j+n*(i-1))

# 출력
for i in range(n):
    for j in range(n):
        print(result[i][j], end =' ')
    print()
