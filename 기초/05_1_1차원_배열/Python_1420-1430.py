# 1420: 3등 찾기
n = int(input())
li = []
score = []
for i in range(n):
    a, b = input().split()
    li.append((a,int(b)))
    score.append(int(b))
score.sort()
for i, j in li:
    if j == score[-3]:
        print(i)


# 1425: 자리 배치
N, C = map(int, input().split())
inp = input().split()
inp.sort()
for i in range(1, N+1):
    if i%(C+1)==0: 
        print()
        print(inp[i-1], end =' ')
    else:
        print(inp[i-1], end =' ')


# 1430: 기억력 테스트 2
N = int(input())
N_num = list(map(int, input().split()))
N_num[:N+1]
M = int(input())
M_q = list(map(int, input().split()))
for i in range(M):
    if M_q[i] in N_num:
        print(1, end =' ')
    else: print(0, end =' ')
