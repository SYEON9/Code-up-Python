# 1172: 세 수 정렬하기
a,b,c = map(int, input().split())
li = sorted([a,b,c])
for i in li: print(i, end=' ')


# 1173: 30분전
h, m = map(int, input().split())
# i
if h!=0:
    if m<30: 
        h -= 1
        m = m+30
    elif m>=30:
        m = m-30
elif h==0:
    if m<30: 
        h = 23
        m = m+30
    elif m>=30:
        m = m-30
print(h,m)

# ii
if m<30:
    m = m+30
    if h==0:
        h=23
    elif h!=0:
        h-=1
else:
    m = m-30
print(h,m)


# 1174: 만능 휴지통
n = int(input())
t = n/10
o = n%10
result = int(o+t)**2
if result>99 or result<1: 
    result = result%100
print(result)
if result<=50: print('GOOD')
else: print('OH MY GOD')
