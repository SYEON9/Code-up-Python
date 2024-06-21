# 6076
"""
# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
"""
n = int(input())
for i in range(0,n+1):
    print(i)


# 6077
"""
정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.
"""
n = int(input())
total = 0
for i in range(1,n+1):
  if i%2==0:
    total+=i
print(total)


# 6078
"""
영문 소문자 'q'가 입력될 때까지
입력한 문자를 계속 출력하는 프로그램을 작성해보자.
"""
while True:
    n = input()
    print(n)
    if n=='q': break
