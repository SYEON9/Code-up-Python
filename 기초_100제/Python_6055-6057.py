# 6055
# 2개의 정수값이 입력될 때,
# 그 불 값이 하나라도 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.
a,b = map(bool,map(int, input().split()))
print(a|b)


# 6056
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.
a,b = map(bool,map(int, input().split()))
print(a&(not b)|(not a)&b)


# 6057
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.
a, b = map(bool, map(int, input().split()))
print((not a) & (not b)|(a&b))
