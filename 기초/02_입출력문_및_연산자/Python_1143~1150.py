# 1143: 비트 연산자(AND)
a,b = map(int, input().split())
print(a & b)

# 1144: 비트 연산자(OR)
a,b = map(int, input().split())
print(a|b)

# 1147: 비트 연산자(<<)
a,x = map(int, input().split())
print(a<<x)

# 1148: 비트 연산자(>>)
a, x = map(int, input().split())
print(a>>x)

# 1149: 두 수 중 큰 수
a,b = map(int, input().split())
# i
if a>b: print(a)
elif a<b: print(b)
# ii
result = (a if a>b else b)
print(result)

# 1150: 세 수 중 가장 작은 수
a,b,c = map(int, input().split())
result = [a,b,c]
# i 
result.sort()
# ii
result = sorted(result)
print(result[0])


