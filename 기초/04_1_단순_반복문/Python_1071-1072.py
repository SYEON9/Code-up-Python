# 1071
a = list(map(int,input().split()))
for i in a:
  if i==0: break
  else: print(i)

# 1072: 정수 입력받아 계속 출력하기
n = int(input())
a = input().split()
if len(a) == n:
    for i in a:
        print(int(i))
