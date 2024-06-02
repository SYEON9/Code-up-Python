# 6019: 기초-입출력
# "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.
y, m, d = input().split(',')
print(f'{d}-{m}-{y}')



# 6020: 기초-입출력
# 주민번호는 다음과 같이 구성된다.
# XXXXXX-XXXXXXX
# 왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.
# '-'를 제외한 주민번호 13자리를 모두 붙여 출력한다.
fro, back = input().split('-')
print(f'{fro}{back}')

# 다른 사용자 답안
fro, back = input().split('-')
print(fro+back)            # case1
print(fro, back, sep='')   # case2



# 6021: 기초-입출력
# 알파벳과 숫자로 이루어진 단어 1개가 입력된다.
# 입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다.
word = input()
for i in range(len(word)):
    print(word[i])
