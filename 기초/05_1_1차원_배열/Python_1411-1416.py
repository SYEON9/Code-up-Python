# 1411: 빠진 카드
N = int(input())
result = [i for i in range(1, N+1)]
while len(result)!=1:
    check = int(input())
    result.remove(check)
print(result[0])


# 1412: 알파벳 개수 출력하기
# -----------------------------------# 
# i.set() 활용
# -----------------------------------# 
# input
english = input()
# 알파벳 set 만들기
result = {}
for i in range(ord('a'), ord('z')+1):
    result[chr(i)] = 0
# input 알파벳 개수 세기
for i in english:
    if i in result.keys():
        result[i] += 1
# 결과 출력
for i in result.keys():
    print(f'{i}:{result[i]}')

# -----------------------------------# 
# ii. list 활용
# -----------------------------------# 
english = input()
li = [0 for _ in range(ord('a'), ord('z')+1)]
for i in english:
    if i>='a' and i<='z':
        li[ord(i)-97] += 1

for i in range(ord(
    'a'), ord('z')+1):
    print('%c:%d' %(chr(i), li[i-97]))


# 1416: 2진수 변환
n = int(input())
print(bin(n)[2:])
