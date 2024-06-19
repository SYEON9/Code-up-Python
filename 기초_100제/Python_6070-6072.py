# 6070
"""
월이 입력될 때 계절 이름이 출력되도록 해보자.

월 : 계절 이름
12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall
"""
a = int(input())
if a==12 or a==1 or a==2:
    print('winter')
elif a==3 or a==4 or a==5:
    print('spring')
elif a==6 or a==7 or a==8:
    print('summer')
else:
    print('fall')

# answer 2
a = int(input())
if a//3 ==1: print('spring')
elif a//3==2: print('summer')
elif a//3==3: print('fall')
else: print('winter')


# 6071
# 임의의 정수가 줄을 바꿔 계속 입력된다.
# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
# (0은 출력하지 않는다.)
n=1
while n!=0:
    n = int(input())
    if n!=0:
        print(n)


# 6072
# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
n = int(input())
for i in range(n,0,-1):
    print(i)

# answer2
a = int(input())
while a !=0:
    print(a)
    a-=1
