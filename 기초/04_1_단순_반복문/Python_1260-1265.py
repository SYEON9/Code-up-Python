# 1260: 3의 배수의 합
a, b = map(int, input().split())
sum = 0
for i in range(a, b+1):
    if i%3==0: sum+=i
print(sum)


# 1261: First Speical Judge(Test)
a = input().split()
li = list()
for i in a:
    if int(i)%5==0: 
        li.append(int(i))
print(li[0])


# 1265: 구구단 출력하기1
n = int(input())
for i in range(1, 10):
    print(f'{n}*{i}={n*i}')
