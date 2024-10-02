# 1132: 문자열 출력하기
print(input())


# 1133: 공백이 있는 문자열 입출력
print(input())


# 1295: 알파벳 대소문자 변환
s = input()
s2 = ''
for i in s:
    if i.islower(): s2 += i.upper()
    elif i.isupper(): s2 += i.lower()
    else: s2 += i
print(s2)
