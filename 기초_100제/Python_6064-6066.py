# 6064
# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.
a,b,c = map(int, input().split())
k = min([a,b,c])
print(k)

# answer
a,b,c = map(int, input().split())
k = a if a<b else b
k2 = k if k<c else c
print(k2)



# 6065
# 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.
a,b,c = map(int, input().split())
li = [a,b,c]
for i in li:
    if i%2==0:
        print(i)


# 6066
# 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
a,b,c=map(int, input().split())
li = [a,b,c]
for i in li:
    if i%2==0: print('even')
    else: print('odd')
