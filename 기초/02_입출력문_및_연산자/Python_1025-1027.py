# 1025-정수 1개 입력받아 나누어 출력하기
a = input()
len_a = len(a)
k=0
for i in range(len_a-1,0,-1):
    print([int(a[k]+'0'*i)])
    k+=1
print([int(a[k])])

# 1025-2
a = input()
print("["+str(int(n[0])*10000)+"]")
print('['+str(int(n[1])*1000)+']')
print('['+str(int(n[2])*100)+']')
print('['+str(int(n[3])*10)+']')
print('['+str(int(n[4])*1)+']')



# 1026-시분초 입력받아 분만 출력하기
h,m,s = input().split(':')
print(m)



# 1027-년월일 입력 받아 형식 바꿔 출력하기
h,m,s = input().split('.')
print(f'{s}-{m}-{h}')
