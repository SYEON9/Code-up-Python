# 1414: C언어를 찾아라
n = input().lower()
result1=0
result2=0
for i in n:
    if i=='c':
        result1 += 1
for i in range(len(n)-1):
    if n[i]+n[i+1] == 'cc':
        result2 += 1
print(result1)
print(result2)


# 1418: t를 찾아라
n = input()
for i in range(len(n)):
    if i == 't':
        print(i+1, end =' ')


# 1419: love 2
n = input()
co = 0
for i in range(len(n)):
    if n[i] == 'l' and n[i:i+4] == 'love': 
        co += 1
print(co)
