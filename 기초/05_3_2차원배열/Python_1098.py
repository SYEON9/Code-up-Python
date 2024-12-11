# 1098: 설탕과자 뽑기
import numpy as np
h, w = map(int, input().split())
n = int(input())

result = np.zeros((h,w))
for i in range(n):
    inp = input().split()
    inp = [int(i) for i in inp]
    print(inp)
    if inp[1] == 0:
        for j in range(inp[0]):
            result[inp[2]-1][inp[3]+j-1] = 1
    elif inp[1] == 1:
        for j in range(inp[0]):
            result[inp[2]-1+j][inp[3]-1] = 1

for i in range(result.shape[0]):
    for j in range(result.shape[1]):
        print(int(result[i][j]), end=' ')
    print()
