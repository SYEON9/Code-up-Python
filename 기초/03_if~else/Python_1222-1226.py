# 1222: 축구의 신2
now, class1, class2 = map(int, input().split())
left = 90-now
if left%5==0: 
    score = left/5
    class1 = class1+score
    if class1>class2: print('win')
    elif class1==class2: print('same')
    else: print('lose')
else:
    score = left/5+1
    class1 = class1+score
    if class1>class2: print('win')
    elif class1==class2: print('same')
    else: print('lose')


# 1224: 분수 크기 비교
a,b,c,d = map(int, input().split())
cond1 = a/b
cond2 = c/d
if cond1>cond2: print('>')
elif cond1==cond2: print('=')
else: print('<')


# 1226: 이번 주 로또
answer = list(map(int, input().split()))
mine = list(map(int, input().split()))
count = 0
plus = answer.pop()
answer
for i in mine:
    if i in answer: count += 1

if count == 6: print('1등')
elif count == 5: 
    if plus in mine: print('2등')
    else: print('3등')
elif count == 4: print('4등')
elif count == 3: print('5등')
else: print('꽝')
