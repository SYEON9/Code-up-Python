# 1055: 하나라도 참이면 참 출력하기
a,b = map(int, input().split())
# i
if a+b>=1: print(1)
else: print(0)

# ii
if bool(a) or bool(b): print(1)
else: print(0)


# 1056: 참/거짓이 서로 다를 때에만 참 출력하기
a,b = map(int, input().split())
# i
if a+b==1: print(1)
else: print(0)

# ii
if (bool(a)==True and bool(b)==False) or (bool(a)==False and bool(b)==True):
    print(1)
else: print(0)


# 1057: 참/거짓이 서로 같을 때에만 참 출력하기
a,b = map(int, input().split())
a2 = bool(a)
b2 = bool(b)
# i
if a2==b2: print(1)
else: print(0)
# ii 
int(a2==b2)
