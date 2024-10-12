# 6131: 일차 방정식 ax+-b=c의 해 구하기
a,b,c= map(int,input().replace('=','x').split('x'))
result = (c-b)/a
print('%.2f' %result)
