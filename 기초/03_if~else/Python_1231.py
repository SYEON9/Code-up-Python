# 1231: 계산기1
intp = input()
li = ['+','-','*','/']
for i in li:
    if i in intp: 
        a,b = map(int, intp.split(i))
        o = i

if o == '+': print(a+b)
elif o == '-': print(a-b)
elif o == '*': print(a*b)
elif o == '/': print(a/b)
