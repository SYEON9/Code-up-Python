# 1284: 암호 해독
# 소수 판별 함수
def isPrime(num):
    # 소수인지 판별하기 위해서 num의 제곱근까지의 값이 필요함
    limit = int(num**0.5)+1
    for i in range(2, limit):
        if num%i==0: 
            return False
    return True

num = int(input())
limit_n = int(num**0.5)+1
for i in range(2, limit_n):
    if num%i==0 and isPrime(i) and isPrime(num//i):
        print(i, num//i)
        break
else:
    print('wrong number')


# 1285: 계산기 2
operations = ['+','-','*','/','=']
num = input()
n = ''
sp = ''
result = 0
for i in num:
    if i in operations: 
        n = int(n)
        if sp == '':
            result = n
        # 부호에 따른 계산
        elif sp == '+':
            result += n
        elif sp == '-':
            result -= n
        elif sp == '*':
            result *=n
        elif sp == '/':
            result //= n  # 정수형 결과가 나오도록 '//'를 사용한다.
        # n과 연산기호 초기화
        n = ''
        sp = i
    else:
        n+= i
print(result)


# 1286: 최댓값, 최솟값
s = []
for i in range(5):
    n = int(input())
    s.append(n)
s.sort()
print(s[-1])
print(s[0])

