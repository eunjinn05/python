# 문자열
sentence = """이렇게하면
두줄가능"""
print(sentence)

#슬라이싱
jumin = '930308-1234567'
print("성별 : ",jumin[7])
print("연도 : ", jumin[0:2]) # 0 ~ 2 미만
print("월 : ", jumin[2:4]) # 2 ~ 4 미만
print("일 : ", jumin[4:6]) # 4 ~ 6 미만
print("생년월일 : ", jumin[:6]) # 0 ~ 6 미만
print("뒷 번호 : ", jumin[7:])
print("뒷 번호 (뒤에서부터) : ", jumin[-7:])

#문자 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace('Python', "Java"))

index = python.index('n')
print(index)
index = python.index('n', index+1) # 다음 숫자 index
print(index)
index = python.find('n') # 같지만 없는 값일때 -1 출력


#문자열포맷
print("나는 %d살입니다." %20)
print("나는 %s를 좋아해요" % "파이썬")
print("Apple은 %c로 시작해요" %"A")
print("나는 %s와 %s를 좋아해요" % ("자몽", "오렌지"))

print("나는 {}살입니다".format(20))
print("나는 {}와 {}를 좋아해요".format("파란색", "초록색"))
print("나는 {1}와 {0}를 좋아해요".format("파란색", "초록색"))

print("나는 {age}살이며 {fruit}를 좋아해요".format(age = 20, fruit = "청포도"))

age = 20
color = "파란색"
print(f"나는 {age}살이며 {color}를 좋아해요")

#퀴즈
url = "http://naver.com"

url = url.replace('http://', '')
index = url.find('.')
url = url[:index]
password = url[:3] + str(len(url)) + str(url.count('e')) + '!'
print(password)