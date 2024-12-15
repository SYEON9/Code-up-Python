# 1099: 성실한 개미
result = [[1,1,1,1,1,1,1,1,1,1],
          [1,0,0,1,0,0,0,0,0,1],
          [1,0,0,1,1,1,0,0,0,1],
          [1,0,0,0,0,0,0,1,0,1],
          [1,0,0,0,0,0,0,1,0,1],
          [1,0,0,0,0,1,0,1,0,1],
          [1,0,0,0,0,1,2,1,0,1],
          [1,0,0,0,0,1,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,1,1,1,1,1,1,1,1,1]]

i = 1
j = 1
while i <= 9 and j <= 9:
    if result[i][j] == 0:
        result[i][j] = 9
        j += 1
    elif result[i][j] == 1:
        i += 1
        j -= 1
        if result[i][j] == 1:
            break
    elif result[i][j] == 2:
        result[i][j] = 9
        break
    
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end =' ')
    print()


