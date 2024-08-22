# 1073: 0 입력될 때까지 무한 출력하기2
a = input().split()
for i in a:
    if int(i)!=0:
        print(i)
    else:
        break


# 1074: 정수 1개 입력받아 카운트다운 출력하기1
n = int(input())
for i in range(n, 0, -1):
    print(i)


# 1075: 정수 1개 입력받아 카운트다운 출력하기2
n = int(input())
for i in range(n, -1, -1):
    print(i)
