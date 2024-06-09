# 6037
# 반복 횟수와 문장을 입력받아 여러 번 출력해보자.
n = input()
s = input()
print(int(n)*s)


# 6038
# 정수 2개(a, b)를 입력받아
# a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.
# 2개의 정수(a, b)가 공백으로 구분되어 입력된다.   2 10
a, b = input().split()
a = int(a)
b = int(b)
c = a**b
print(c)


# 6039
# 실수 2개(f1, f2)를 입력받아
# f1을 f2번 거듭제곱한 값을 출력하는 프로그램을 작성해보자.
# 2개의 실수(f1, f2)가 공백으로 구분되어 입력된다.
a,b = input().split()
a = float(a)
b = float(b)
print(a**b)


# 6040
# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.
# 2개의 정수(a, b)가 공백으로 구분되어 입력된다.
a, b = input().split()
a = int(a)
b = int(b)
print(a//b)


# 6041
# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.
# 2개의 정수(a, b)가 공백으로 구분되어 입력된다.
a,b = input().split()
a = int(a)
b = int(b)
print(a%b)


# 6042
# 실수 1개를 입력받아
# 소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력해보자.
n = input()
n = float(n)
print(round(n,2))
print(format(n, '.2f'))


