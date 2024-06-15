# 6058
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.
a, b = map(bool, map(int, input().split()))
print(not (a|b))


# 6059
# 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.
# 비트단위(bitwise)연산자 ~ 를 붙이면 된다.(~ : tilde, 틸드라고 읽는다.)
a = int(input())
print(~a)


# 6060
# 입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.
# 비트단위(bitwise)연산자 &를 사용하면 된다.(and, ampersand, 앰퍼센드라고 읽는다.)
a,b  = map(int, input().split())
print(a&b)
