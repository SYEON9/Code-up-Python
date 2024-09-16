# 1295: 알파벳 대소문자 변환
n = input()
result = ''
for i in n:
    if i.isupper(): result += i.lower()
    elif i.islower(): result += i.upper()
    else: result += i
print(result)


# 1675: 시저의 암호1
n = input()
result = ''
for i in n:
    if i == 'a': result += 'x'
    elif i == 'b': result += 'y'
    elif i == 'c': result += 'z'
    elif i == ' ': result += ' '
    else: 
        result += chr(ord(i)-3)
print(result)


# 1294: 시저의 암호2
n = input()
result = ''
for i in n:
    if i == 'x': result += 'a'
    elif i =='y': result += 'b'
    elif i == 'z': result += 'c'
    elif i == ' ': result += ' '
    else: result += chr(ord(i)+3)
print(result)
