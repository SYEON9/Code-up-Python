# 1254: 알파벳 출력하기
a, b = input().split()
for i in range(ord(a), ord(b)+1):
    print(chr(i), end=' ')


# 1255: 두 실수 사이 출력하기
a,b = map(float, input().split())
while a<=b:
    print('%.2f' % a, end = ' ')
    a+=0.01


# 1256: 별 출력하기
n = int(input())
print(n*'*')
