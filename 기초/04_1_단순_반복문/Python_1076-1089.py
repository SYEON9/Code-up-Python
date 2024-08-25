# 1076: 문자 1개 입력받아 알파벳 출력하기
###
아스키코드 변환함수 ord, chr
- ord(): 문자 -> 숫자
- chr(): 숫자 -> 문자
# i
s = input()
for i in range(ord('a'), ord(s)+1):
    print(chr(i). end= ' ')
# ii
c = input()
n = ord(c)
i = ord('a')
while i<=n:
    print(chr(i), end=' ')
    i+=1


# 1077: 정수 1개 입력받아 그 수까지 출력하기
# i
n = int(input())
for i in range(n+1):
    print(i)
# ii
n = int(input())
s = 0
while s <= n:
    print(s)
    s += 1


# 1078: 짝수 합 구하기
# i
n = int(input())
count = 0
for i in range(n+1):
    if i%2 == 0: 
        count += i
print(count)

# ii
n = int(input())
s = 0
count = 0
while s <= n:
    if s%2==0: count += s
    s += 1
print(count)


# 1079: 원하는 문자가 입력될 때까지 반복 출력하기
answer = 'q'
s = input().split()
for i in s:
    print(i)
    if i == answer: break


# 1080: 언제까지 더해야 할까?
n = int(input())
s = 1
count = 1
while s < n:
    s =  s + count
    count = count + 1
print(count-1)


# 1083: 3 6 9 게임의 왕이 되자!
n = int(input())
for i in range(1, n+1):
    if i%3 == 0: print('X', end = ' ')
    else: print(i, end = ' ')


# 1087: 여기까지! 이제 그만~
n = int(input())
s = 0
count = 1
while s < n:
    s += count
    count += 1
print(s)


# 1088: 3의 배수는 통과?
n = int(input())
for i in range(1, n+1):
    if i%3 ==0: continue
    else: print(i, end = ' ')


# 1089: 수 나열하기1
a, b, n = map(int, input().split())
result = a + (b*(n-1))
print(result)
