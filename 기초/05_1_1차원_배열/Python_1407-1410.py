# 1407: 문자열 출력하기 1
# i
n = int()
print(n.replace(' ',''))
# ii
n = input().split()
for i in n:
    print(i, end ='')


# 1409: 기억력 테스트 1
int = input().split()
k = int(input())
print(int[k])


# 1410: 올바른 괄호 1(괄호 개수 세기)
s = input()
count_open = 0
count_close = 0
for i in s:
    if i == '(': count_open+=1
    elif i == ')': count_close += 1
print(count_open, end ='')
print(count_close)
