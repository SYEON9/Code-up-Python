# 1163: 당신의 사주를 봐 드립니다2
y, m, d = map(int, input().split())
result = int(y+m+d/100)%10         # (y+m+d)%1000//100
print('대박' if result%2==0 else '그럭저럭')


# 1164: 터널 통과하기1
a, b, c = map(int, input().split())
if a > 170 and b > 170 and c > 170: print('PASS')
else: print('CRASH')


# 1165: 축구의 신1
time, score = map(int, input().split())
time_limit = 90-time
if time_limit%5 == 0:
    extra_score = time_limit//5 
else: 
    extra_score = time_limit//5 +1
print(score + extra_score)
