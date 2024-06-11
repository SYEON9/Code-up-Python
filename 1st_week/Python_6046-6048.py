# 6046
# 정수 1개를 입력받아 2배 곱해 출력해보자.
n = int(input())
print(n*2)
print(n<<1)


# 6047
# 정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.
# 0 <= a <= 10, 0 <= b <= 10
a, b = input().split()
a = int(a)
b = int(b)
print(a<<b)
print(a*(2**b))


# 6048
# 두 정수(a, b)를 입력받아
# a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.
a,b = input().split()
a = int(a)
b = int(b)
if a<b: print('True')
else: print('False')
