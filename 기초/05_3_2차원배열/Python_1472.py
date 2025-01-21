# 1472: 2차원 배열 지그재그 채우기 2-5
# 입력
n, m = map(int, input().split())

# 배열 채우기
result = []
for i in range(n):
    result.append([])

inp = 1
check = True        # n이 짝수
if n%2 != 0:        # n이 홀수
    check = False

# check= True
if check:
    for i in range(n-1, -1, -1):
        if i%2!=0:
            for j in range(m):
                result[i].insert(0, inp)
                inp += 1
        else:
            for j in range(m):
                result[i].append(inp)
                inp += 1

else:
    for i in range(n-1, -1, -1):
        if i%2==0:
            for j in range(m):
                result[i].insert(0, inp)
                inp += 1
        else:
            for j in range(m):
                result[i].append(inp)
                inp += 1


# 출력
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end=' ')
    print()
