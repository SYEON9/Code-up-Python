# 6067
# 0이 아닌 정수 1개가 입력되었을 때, 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.
# 음수이면서 짝수이면, A
# 음수이면서 홀수이면, B
# 양수이면서 짝수이면, C
# 양수이면서 홀수이면, D
# 를 출력한다.
a= int(input())
if a<0:
    if a%2==0: print('A')
    else: print('B')
elif a>0:
    if a%2==0: print('C')
    else: print('D')


# 6068
"""
# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.
평가 기준
점수 범위 : 평가
 90 ~ 100 : A
 70 ~   89 : B
 40 ~   69 : C
   0 ~   39 : D
로 평가되어야 한다.
"""
a = int(input())
if a>= 90 and a<=100: print('A')
elif a>=70 and a<=89: print('B')
elif a>=40 and a<=69: print('C')
else: print('D')


# 6069
"""
평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

평가 내용
평가 : 내용
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?
"""
a = input()
if a=='A': print('best!!!')
elif a=='B': print('good!!')
elif a=='C': print('run!')
elif a=='D': print('slowly~')
else: print('what?')
