# 6091
a,b,c = map(int, input().split())
d = 1
while d%a!=0 or d%b!=0 or d%c!=0:
    d+=1
print(d)


# 6092
n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

d = []
for i in range(24) :
  d.append(0)

for i in range(n) :
  d[a[i]] += 1

for i in range(1, 24) :
  print(d[i], end=' ')


# 6093
n = int(input())
a = input().split()

for i in range(n-1,-1,-1):
    print(a[i], end=' ')
