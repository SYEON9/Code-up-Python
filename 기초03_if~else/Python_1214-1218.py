# 1214: 이 달은 며칠까지 있을까?
yy, m = map(int, input().split())

odd = [1,3,5,7,8,10,12]
bin = [4,6,9,11]
if m==2:
    if yy%400==0 or (yy%4==0 and yy%100!=0): print(29)
    else: print(28)
elif m in odd: print(31)
elif m in bin: print(30)


# 1216: 컨덜팅 회사
income_n, income_a, a = map(int, input().split())
result_a = income_a-a
if income_n>result_a: print('do not advertise')
elif income_n<result_a: print('advertise')
else: print('does not matter')


# 1218: 삼각형 판단하기
a,b,c = map(int, input().split())
if a==b==c: print('정삼각형')
elif a==b!=c or a!=b==c or a==c!=b: print('직각삼각형')
el: print('삼각형')
