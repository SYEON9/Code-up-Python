# 6052
# 정수가 입력되었을 때, True/False 로 평가해주는 프로그램을 작성해보자.
n = int(input())
print(bool(n))


# 6053
# 정수값이 입력될 때,
# 그 불 값을 반대로 출력하는 프로그램을 작성해보자.
n = int(input())
print(bool(not n))


# 6054
# 2개의 정수값이 입력될 때,
# 그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.
a,b = map(bool, map(int, input().split()))
print(a&b)
# a, b = input().split()
# print(bool(int(a)) and bool(int(b)))
