# 1154: 큰수-작은수
a,b = map(int, input().split())
print(abs(a-b))


# 1155: 7의 배수
a = int(input())
# i
if a%7==0: print('multiple')
else: print('not multiple')
# ii
print('multiple' if a%7==0 else 'not multiple')


# 1156: 홀수 짝수 구별
a = int(input())
print('odd' if a%2==1 else 'even')


# 1157: 특별한 공 던지기 1
score = float(input())
print('win' if score>=50 and score<=60 else 'lose')


# 1158: 특별한 공 던지기 2
score = float(input())
print('win' if score>=30 and score<=40 and score>=60 and score<=70 else 'lose')


# 1159: 특별한 공 던지기 3
score = float(input())
cond1= (score>=50 and score<=70)
cond2 = (score%6==0)
print('win' if cond1 or cond2 else 'lose')


# 1160: 아르바이트 가는 날
work = [1,3,5,7]
not_work = [2,4,6]
he = int(input())
print('oh my god' if he in work else 'enjoy')


# 1161: 홀수와 짝수 그리고 더하기
a,b = map(int, input().split())
result = a+b
if a%2==0: print('짝수+', end='')
else: print('홀수+', end='')
if b%2==0: print('짝수', end ='')
else: print('홀수', end ='')
if result%2==0: print('=짝수')
else: print('=홀수')


# 1162: 당신의 사주를 봐 드립니다 1
y,m,d = map(int, input().split())
result = y-m+d
print('대박' if result%10==0 else '그럭저럭')
