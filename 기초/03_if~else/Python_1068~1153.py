# 1068: 정수 1개 입력받아 평가 출력하기
score = int(input())
if score>=90 and score<=100: print('A')
elif score>=70 and score<=89: print('B')
elif score>40 and score<=69: print('C')
elif score>=0 and score<=39: print('D')

# 1069: 평가 입력받아 다르게 출력하기
score = input()
if score=='A': print('best!!!')
elif score == 'B': print('good!!')
elif score == 'C': print('run!')
elif score == 'D': print('slowly~')
else: print('what?')

# 1070: 월 입력받아 계절 출력하기
season = int(input())
if season == 12 or season == 1 or season == 2: print('winter')
elif season == 3 or season == 4 or season == 5: print('spring')
elif season == 6 or season == 7 or season == 8: print('summer')
elif season == 9 or season == 10 or season == 11: print('fall')

# 1151: 10보다 작은 수
a = int(input())
if a<10: print('small')

# 1152: 10보다 작은 수(else 버전)
a = int(input())
if a<10: print('small')
else: print('big')

# 1153: 두 수의 대소 비교
a,b = map(int, input().split())
if a>b: print('>')
elif a<b: print('>')
else: print('=')
