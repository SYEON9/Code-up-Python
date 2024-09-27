# 1402: 거꾸로 출력하기 3
n = int(input())
li = input().split()
for i in range(len(li)-1, -1, -1):
    print(li[i], end =' ')


# 1403: 배열 두번 출력하기
k = int(input())
inp = input().split()
for i in range(2):
    for j in inp:
        print(j)


# 1405: 숫자 로테이션
n = input()
inp = input().split()
for i in range(5):
    for j in inp:
        print(j, end = ' ')
    print()
    value = inp[0]
    del inp[0]
    inp.append(value)
