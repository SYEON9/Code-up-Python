# 1096: 바둑판에 흰 돌 놓기
import numpy as np

n = int(input())
result = np.zeros((19,19))
c = 0
while c<n:
    x,y = map(int, input().split())
    result[x-1][y-1] = 1
    c += 1
for i in range(19):
    for j in range(19):
        print(int(result[i][j]), end =' ')
    print()


# 1097: 바둑알 십자 뒤집기
