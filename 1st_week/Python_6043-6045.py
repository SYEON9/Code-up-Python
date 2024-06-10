#------------------------------------------------#
# 6043
# 실수 2개(f1, f2)를 입력받아
# f1 을 f2 로 나눈 값을 출력해보자. 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.
# my code
n1, n2 = input().split()
n1 = float(n1)
n2 = float(n2)
print(round(n1/n2,3))

# other user code
n1, n2 = map(float, input().split())
f= n1/n2
print('%0.3f' % f)


#------------------------------------------------#
# 6044
# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
# 단, b는 0이 아니다.
n1, n2 = map(int, input().split())
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1//n2)
print(n1%n2)
print(round(n1/n2,2))


# ------------------------------------------------#
# 6045
# 정수 3개를 입력받아 합과 평균을 출력해보자.
a,b,c = map(int,input().split())
plus = a+b+c
mean = plus/3
print(plus, '%0.2f' % mean)
