# 1440: 비교
n = int(input())
num = list(map(int, input().split()))
for i in range(len(num)):
    result = num.copy()
    check = result[i]
    del result[i]
    print(f'{i+1}:', end =' ')
    for j in range(len(result)):
        if result[j]>check: print('<', end =' ')
        elif result[j]==check: print('=', end =' ')
        elif result[j]<check: print('>', end =' ')
    print()
