# 1382: GuguClass
# i
for i in range(1, 10):
    for j in range(2, 6):
        if j==5: 
            if i*j < 10: print(f'{j} x {i} =  {j*i}', end = '\n')
            else: 
                print(f'{j} x {i} = {j*i}', end = '\n')
        else:
            if i*j < 10: print(f'{j} x {i} =  {j*i}', end = '\t')
            else: 
                print(f'{j} x {i} = {j*i}', end = '\t')

# ii: String formatting을 사용하면 간단하게 코드를 작성할 수 있다.
for i in range(1, 10):
    for j in range(2, 6):
        if j==5: 
            print('%d x %d = %2d' %(j, i, j*i), end = '\n')
        else:
            print('%d x %d = %2d' %(j, i, j*i), end = '\t')


# 1677: 종이 자르기
n, m = map(int, input().split())
for i in range(m):
    if i == 0 or i == m-1:
        re = (n-2)*'-'
        print(f'+{re}+')
    else:
        re = ' '*(n-2)
        print(f'|{re}|') 


# 3122: 마름모 출력하기 2
n = int(input())
pl = 0
for i in range(1, n+1):
    print(' '*(n-i), end ='')
    print('*'*(pl+i), end ='')
    print('*'*(i-1))
for i in range(n-1, 0, -1):
    print(' '*(n-i), end ='')
    print('*'*(pl+i), end ='')
    print('*'*(i-1))
