# 6034
# 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.
# 2개의 정수가 공백으로 구분되어 입력된다.
a,b = input().split()   # 123 -123
a = int(a)
b = int(b)
print(a-b)              # 246


# 6035
# 실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.
# 2개의 실수가 공백으로 구분되어 입력된다.
a,b = input().split()   # 2.0*0.5
a = float(a)
b = float(b)
print(a*b)              # 1.0


# 6036
# 단어와 반복 횟수를 입력받아 여러 번 출력해보자.
#단어와 반복 횟수가 공백으로 구분되어 입력된다.
a,n = input().split()   # love 3
print(a*int(n))         # lovelovelove
