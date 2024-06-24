# 6085
w, h, b = map(int, input().split())
result = w*h*b/8/1024/1024
print(result, 'MB')


# 6086
n = int(input())
result = 0
for i in range(1,n+1):
    if result>=n:
        break
    else:
        result+=i
print(result)
### answer2
n = int(input())
c = 0
s = 0
while True:
    s+=c
    c+=1
    if s>=n:
        break

print(s)



# 6087
n = int(input())
result=''
for i in range(n+1):
    if i%3==0:
        continue
    else: 
        result += f'{i}'
        result += " "
print(result)

### answer2
n = int(input())
result=''
for i in range(n+1):
    if i%3==0:
        continue
    else: 
        print(i, end=' ')
  
