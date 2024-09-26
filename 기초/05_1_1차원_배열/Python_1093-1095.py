# 1093: 이상한 출석 번호 부르기1
num = input()
n = input().split()
result = [0 for i in range(23)]
for i in n:
    k = int(i) -1
    result[k] += 1
for i in result:
    print(i, end = ' ')


# 1094: 이상한 출석 번호 부르기 2
n = int(input())
inp = input().split()
result = []
for i in inp:
    result.append(int(i))
for i in range(len(result)-1,-1,-1):
    print(result[i], end = ' ')


# 1095: 이상한 출석 번호 부르기 3
a = int(input())
b = input().split()
result=  []
for i in b:
    result.append(int(i))
result.sort()
print(result[0])
