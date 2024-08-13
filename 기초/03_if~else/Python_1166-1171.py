# 1166: 윤년 판별
a = int(input())
cond1 = (a%400==0)
cond2 = (a%4==0 and a%100!=0)
if cond1 or cond2: print('Leap')
else: print('Normal')


# 1167: 두 번째 수
a,b,c = map(int, input().split())
result = sorted([a,b,c])
print(result[1])


# 1168: 나이 계산1
bday, sex = map(int, input().split())
year = 2012
bday = bday//10000
if sex==1 or sex==2: bday = bday+1900
else: bday = bday+2000
print(year-bday+1)


# 1169: 나이 계산2
age = int(input())-1
year = 2012 - age
if year>=2000: 
    n = 3
else: 
    n=1
year = year%100
print(year, n)


# 1170: 당신의 학번은? 1
a,b,c = map(int, input().split())
if c<10: c = '0'+str(c)
print(a,b,c, sep='')


# 1171: 당신의 학번은? 2
a,b,c = map(int, input().split())
# i
if b<10: b = '0'+str(b)
if c>=10 and c<100: c = '0'+str(c)
elif c<10: c = '00'+str(c)
print(a,b,c, sep='')
# ii
print('%d%02d%03d' %(a,b,c))
