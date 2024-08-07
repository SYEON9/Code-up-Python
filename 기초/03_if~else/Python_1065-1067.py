# 1065: 정수 3개 입력받아 짝수만 출력하기
a,b,c = map(int, input().split())
result = [a,b,c]
# i
for i in result:
    if i%2==0: print(i)
# ii
if a%2==0: print(a)
if b%2==0: print(b)
if c%2==0: print(c)


# 1166: 정수 3개 입력받아 짝/홀 출력하기
a,b,c = map(int, input().split())
# i
if a%2==0: print('even')
else: print('odd')
if b%2==0: print('even')
else: print('odd')
if c%2==0: print('even')
else: print('odd')
# ii
result = [a,b,c]
for i in result:
    if i%2==0: print('even')
    else: print('add')
# iii
result = [a,b,c]
for i in result:
    print('even' if i%2==0 else 'odd')


# 1067: 정수 1개 입력받아 분석하기
a = int(input())
# i
if a>0: print('plus')
elif a<0: print('minus')
if a%2==0: print('even')
else: print('odd')
#ii

