# 1228: 비만도 측정1
height, weight = map(float, input().split())
standard_weight = (height - 100)*0.9
score = (weight-standard_weight)*100/standard_weight

if score<=10: print('정상')
elif score >10 and score<=20: print('과체중')
else: print('비만')


# 1229: 비만도 측정2
height, weight = map(float, input().split())
if height<150: standard_weight = (height-100)
elif height>=150 and height<160: standard_weight = (height-150)/2+50
else: standard_weight = (height-100)*0.9

score = (weight-standard_weight)*100/standard_weight
if score<=10: print('정상')
elif score >10 and score<=20: print('과체중')
else: print('비만')


# 1230: 터널 통과하기2
a,b,c = map(int, input().split())
height=170
if a<=height: print('CRASH', a)
elif b<=height: print('CRASH', b)
elif c<=height: print('CRASH', c)
