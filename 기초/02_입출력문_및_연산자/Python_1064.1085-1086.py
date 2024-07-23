# 1064: 정수 3개 입력받아 가장 작은 수 출력하기
a,b,c = map(int, input().split())
result = a if a<b else (b if b<c else (c if c<a else a))
print(result)

# 1085: 소리 파일 저장용량 계산하기
h, b, c, s = map(int, input().split())
result = (h*b*c*10)/8/1024/1024
print(result)


# 1086: 그림 파일 저장용량 계산하기
a,b,c = map(int, input().split())
result = (a*b*c)/8/1024/1024
print(round(result,2), 'MB'))
