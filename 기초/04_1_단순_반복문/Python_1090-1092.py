# 1090: 수 나열하기2
a,r,n = map(int, input().split())
result = a*(r**(n-1))
print(result)


# 1091: 수 나열하기3
a,m,d,n = map(int, input().split())
for i in range(n-1):
    a = a*m+d
print(a)


# 1092: 함께 문제 푸는 날
x,y,z = map(int, input().split())
d=1
while (d%x!=0 or d%y!=0 or d%z!=0):
    d+=1
print(d)
