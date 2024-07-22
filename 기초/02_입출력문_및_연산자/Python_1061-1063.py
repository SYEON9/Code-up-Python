# 1061: 비트단위로 or 하여 출력하기
a,b = map(int, input().split())
print(a|b)


# 1062: 비트단위로 xor 하여 출력하기
a,b = map(int, input().split())
print(a^b)


# 1063: 두 정수 입력받아 큰 수 출력하기
a,b = map(int, input().split())
# i
if a>b: print(a)
else: print(b)
# ii
c = (a if a>b else b)
print(c)
