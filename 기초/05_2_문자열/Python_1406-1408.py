# 1406: love
n = input()
if n == 'love': print('I love you.')


# 1407: 문자열 출력하기1 
# i
s = input()
if len(s)<=100: s = s.replace(' ',  '')
print(s)
# ii: for문을 이용한 코드
s = input().split()
result = ''
for i in s:
    result += i
print(result)


# 1408: 암호 처리
s = input()
result1 = ''
result2 = ''
for i in s:
    check = ord(i)
    pro1 = check + 2
    pro2 = (check*7)%80+48
    result1 += chr(pro1)
    result2 += chr(pro2)
print(result1)
print(result2)
