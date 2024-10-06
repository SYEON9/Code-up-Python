# 1733: I.O.I
n = input()
if n=='IOI': print('IOI is the International Olympiad in Informatics.')
else: print("I don't care.")


# 1734: welcome!
n = input()
# i
print(f'welcome! {n}')
# ii
print('welcome! %s' %n)


# 1754: 큰 수 비교
# i
a,b = map(int, input().split())
if a>b: print(b,a)
elif a<b: print(a,b)
# ii
a = list(map(float, input().split()))
a.sort()
for i in range(len(a)):
    print(a[i], end = ' ')


# 1990: 3의 배수 판별하기
n = int(input())
if n%3 == 0: print(1)
else: print(0)


# 2721: 순환 문자열
a = input()
b = input()
c = input()
if a[-1] == b[0] and b[-1] == c[0] and c[-1] == a[0]: print('good')
else: print('bad')


# 6130: 일차 방정식 ax+-b=0 의 해 구하기
n = input()
or = ['+','-']
a, b = int(n.replace('x+', ' ').replace('x-', ' ').split())
result = round(-b/a,2)
print(result)

