# 1207: 윷놀이
a,b,c,d = map(int, input().split())
result = a+b+c+d
if result==1: print('도')
elif reuslt==2: print('개')
elif result==3: print('걸')
elif result==4: print('윷')
elif result==0: print('모')


# 1210: 칼로리 계산하기
a,b = map(int, input().split())
menu = {1:400, 2:340, 3:170, 4:100, 5: 70}
result = menu[a]+menu[b]
if result>500: print('angry')
elif result<=500: print('no angry')


# 1212: 삼각형의 성립 조건
a,b,c = map(int, input().split())
check = sorted([a,b,c])
max = check[2]
oth1 = check[0]
oth2 = check[1]
if max<oth1+oth2: print('yes')
else: print('no')

