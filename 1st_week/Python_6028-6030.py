# 6028
# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
n = int(input())
print('%X'%n)


# 6029
# 16진수를 입력받아 8진수(octal)로 출력해보자.
a = input()
n = int(a, 16)   # 16인수로 변환
print('%o'%n)


# 6030
# 영문자 1개를 입력받아 10진수 유니코드(Unicode) 값으로 출력해보자.
a = input()
n = ord(a)    # 10진수 unicode로 변환.
print(n)
