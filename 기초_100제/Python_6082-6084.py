# 6082
"""
친구들과 함께 3 6 9 게임을 하던 영일이는 잦은 실수 때문에 계속해서 벌칙을 받게 되었다.
3 6 9 게임의 왕이 되기 위한 369 마스터 프로그램을 작성해 보자.

** 3 6 9 게임은?
여러 사람이 순서를 정한 후, 순서대로 수를 부르는 게임이다.
만약 3, 6, 9 가 들어간 수를 자신이 불러야 하는 상황이라면, 수를 부르는 대신 "박수(X)" 를 쳐야 한다.
33과 같이 3,6,9가 두 번 들어간 수 일때, "짝짝"과 같이 박수를 두 번 치는 형태도 있다. 
"""
result = ''
for i in range(1, n+1):
    i_s = str(i)    
    le = len(i_s)   
    count = 0
    for j in range(le):  
        if int(i_s[j])%3==0:   
            if int(i_s[j])!=0:
                count +=1
                result += 'X'
    if count == 0:
        result += i_s
    result += ' '
print(result)

# 6083
"""
빨강(red), 초록(green), 파랑(blue) 빛을 섞어 여러 가지 다른 색 빛을 만들어 내려고 한다.

빨강(r), 초록(g), 파랑(b) 각 빛의 가짓수가 주어질 때,
주어진 rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합(r g b)과 만들 수 있는 색의 가짓 수를 계산해보자.  

**모니터, 스마트폰과 같은 디스플레이에서 각 픽셀의 색을 만들어내기 위해서 r, g, b 색을 조합할 수 있다.
**픽셀(pixel)은 그림(picture)을 구성하는 셀(cell)에서 이름이 만들어졌다.
"""
r,g,b = map(int, input().split())
count = 0
for r_i in range(r):
    for g_i in range(g):
        for b_i in range(b):
            print(f"{r_i} {g_i} {b_i}")
            count+=1
print(count)

# answer2 
r,g,b = map(int, input().split())
for r_i in range(r):
    for g_i in range(g):
        for b_i in range(b):
            print(r_i, g_i, b_i)
print(r*g*b)


# 6084
"""
소리가 컴퓨터에 저장될 때에는 디지털 데이터화 되어 저장된다.

마이크를 통해 1초에 적게는 수십 번, 많게는 수만 번 소리의 강약을 체크하고,
한 번씩 체크할 때 마다 그 값을 정수값으로 바꾸어 저장하는 방식으로 소리를 파일로 저장할 수 있다.

값을 저장할 때에는 비트를 사용하는 정도에 따라 세세한 녹음 정도를 결정할 수 있고,
좌우(스테레오) 채널로 저장하면 2배… 5.1채널이면 6배의 저장공간이 필요하고,
녹음 시간이 길면 그 만큼 더 많은 저장공간이 필요하다.

1초 동안 마이크로 소리강약을 체크하는 횟수를 h
(헤르쯔, Hz 는 1초에 몇 번? 체크하는가를 의미한다.)

한 번 체크한 값을 저장할 때 사용하는 비트수를 b
(2비트를 사용하면 0 또는 1 두 가지, 16비트를 사용하면 65536가지..)

좌우 등 소리를 저장할 트랙 개수인 채널 개수를 c
(모노는 1개, 스테레오는 2개의 트랙으로 저장함을 의미한다.)

녹음할 시간(초) s가 주어질 때,

필요한 저장 용량을 계산하는 프로그램을 작성해보자.

h, b, c, s 가 공백을 두고 입력된다.
h는 48,000이하, b는 32이하(단, 8의배수), c는 5이하, s는 6,000이하의 자연수이다.

"""
h,b,c,s = map(int, input().split())
result = h*b*c*s/8/1024/1024 
result = round(result, 1)
print(result, 'MB')
