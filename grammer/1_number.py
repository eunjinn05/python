#애완동물을 소개 시켜주세요
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 "+animal+"의 이름은 "+name+"이예요")
print(name+"는 "+str(age)+"살이며, "+hobby+"를 좋아해요")
print(name,"는 ", age,"살이며, ", hobby,"를 좋아해요")
print(name+"이는 어른일까요?"+str(is_adult))

#문제
station = "사당"
print(station,"행 열차가 들어오고있습니다.")

station = "신도림"
print(station,"행 열차가 들어오고있습니다.")

station = "인천공항"
print(station,"행 열차가 들어오고있습니다.")

#숫자
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) #2

print(2**3) #2^3
print(5%2) #나머지
print(5//2) #몫

print((3==0) & (2==0))

print(abs(-5)) #절대값
print(pow(4,2)) # 4^2
print(max(5, 12)) #최댓값
print(min(5, 12)) #최솟값
print(round(3.4)) #반올림

#math import
from math import *
print(floor(3.55)) #버림
print(ceil(4.1)) #올림
print(sqrt(16))  #제곱근 4

#random
from random import *
print(random()) # 0.0 ~ 1.0 미만
print(random() * 10) # 0.0 ~ 10.0 미만
print(int(random() * 10)) # 0 ~ 10 미만

print(randrange(1, 45)) # 1 ~ 45 미만
print(randint(1, 45)) # 1 ~ 45 이하


#퀴즈
day = randint(4, 28)
print("오프라인 스터디 날짜는 매달 ", day,"일로 결정되었습니다")


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

print("나는 {}살입니다".format(20))
print("나는 {}와 {}를 좋아해요".format("파란색", "초록색"))
print("나는 {1}와 {0}를 좋아해요".format("파란색", "초록색"))

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

# 리스트
subway = [10, 20, 30]
print(subway)
subway = ['은딘', '현아', '오짱']

print(subway.index('은딘'))
subway.append('위사')
print(subway)

subway.insert(1, '은딘')
print(subway)

print(subway.pop())
print(subway.count('은딘'))

#리스트 정렬
num_list = [5,3,2,4,1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

#리스트 지우기
num_list.clear()
print(num_list)

#다양한 자료형
mix_list = ['은딘', 30, True]

mix_list.extend(subway)
print(mix_list)

#딕셔너리
cabinet = {3:'A', 6:'B'}
print(cabinet[3])
print(cabinet.get(3))
print(cabinet.get(7, 'no use'))

print(3 in cabinet)

cabinet[7] = 'C'
print(cabinet)

del cabinet[6]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

#튜플
#고정
alpabet = ('A', 'B')
print(alpabet[0])
(A, B, C) = ('X', 'Y', 'Z')
print((A,B,C))

#세트 (집합)
#중복 X, 순서 X
my_set = {1,2,3,3,3,3}
print(my_set)

school = {'성균관대', '고려대', '이화여대'}
in_sinchon = {'이화여대'}

#교집합
print(school & in_sinchon)
print(school.intersection(in_sinchon))

#합집합
print(school | in_sinchon)
print(school.union(in_sinchon))

#차집합
print(school - in_sinchon)
print(school.difference(in_sinchon))

school.add('연세대')
school.remove('고려대')


#자료구조 변경
alpabet = {'a', 'b', 'c'}
print(alpabet, type(alpabet))

alpabet = list(alpabet)
print(alpabet, type(alpabet))

alpabet = tuple(alpabet)
print(alpabet, type(alpabet))

alpabet = set(alpabet)
print(alpabet, type(alpabet))

#퀴즈
from random import *
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(lst)
num = (sample(lst, 1))
lst.remove(num[0])
num2 = (sample(lst, 3))
print('-- 당첨자 발표 --')
print('치킨 당첨자 : ', num[0])
print('커피 당첨자 : ', num2)
print('-- 축하합니다 --')


#if
# weather = input("오늘 날씨가 어때요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else :
#     print("준비물이 필요없습니다")

# temp = int(input("기온은 어때요?"))
# if temp >= 30 :
#     print("너무 더워요")
# elif temp >= 20 and temp < 30 :
#     print("좋아요")
# else :
#     print("추워요")

#for문
# for waiting_no in [0,1,2,3,4,5] :
#     print("대기 번호 : {0}".format(waiting_no))

# for waiting_no in range(1, 6) :
#     print("대기번호 : {0}".format(waiting_no))

#while
# customer = '은딘'
# index = 5
# while index >= 1 :
#     print("{0}, 커피가 나왔습니다. {1}번 남았습니다.".format(customer, index))
#     index -= 1
    
#     if index == 0 :
#         print('커피가 사라졌습니다.')

# customer = '은딘'
# person = ''
# while customer != person :
#     print("{0}님, 커피가 준비되었습니다.".format(customer))
#     person = input('이름이 어떻게되세요?')

#     if person != customer :
#         print('아직 커피가 나오지않았습니다. 기다려주세요')
#     else :
#         print('커피 나왔습니다')

# absent = [3,5]
# no_book = [7,9]
# for student in range(1,20) :
#     if student in absent :
#         continue
#     elif student in no_book :
#         print("{0}번, 책 가져와".format(student))
#         break
#     else :
#         print("{0}번, 책 읽어봐".format(student))

# #한줄 for문
# student = ['emily', 'john', 'emma', 'jane']
# student = [len(i) for i in student]
# print(student)

# student = ['emily', 'john', 'emma', 'jane']
# student = [i.upper() for i in student]
# print(student)

#퀴즈
# i = 0
# for customer in range(1, 51) :
#     time = randrange(5, 51)
#     if time >= 5 and time <= 15 :
#         check = '[O]'
#         i += 1
#     else :
#         check = '[]'
#     print(check,"{0}번째 손님 (소요시간 {1}분)".format(customer, time))
# print('총 탑승 승객 : {0}분'.format(i))

#함수
# def ABCC () :
#     return 'ABC'

# print(ABCC())

# def school_location (name, location) :
#     print(name,'는 ',location,'에 있습니다.')

# school_location("서울대", "관악구")
# school_location(location="신촌", name="연세대")
# school_location(name = "한양대", location = "왕십리")

# def school_data (location, *name) :
#     for school in name :
#         print("{0}에 있는 학교는 {1}입니다".format(location, school))

# print(school_data("신촌", '서강대', '연세대', '이화여대'))

# #퀴즈
# def std_weight (height, gender) :
#     cal_height = height / 10
#     weight = 0
#     if gender == "man" : 
#         weight = (cal_height * cal_height * 22) / 100
#         print("키", height,"cm 남자의 표준 체중은 ", round(weight, 2),'kg 입니다.')
#     elif gender == "woman" :
#         weight = (cal_height * cal_height * 23) /100
#         print("키", height,"cm 여자의 표준 체중은 ", round(weight, 2),'kg 입니다.')

    
# std_weight(175, 'man')

#표준 입출력
print('Python', 'Java', sep=',', end='?') #end 기능 : 끝에 문자 처리하면서 아래 문자까지 붙임
print('가나다')

# import sys
# print('Python', 'Java', file=sys.stdout)
# print('Python', 'Java', file=sys.stderr)

scores = {'수학':50, '국어':80, '코딩':100}
for key, val in scores.items() :
    # print(key, val)
    print(key.ljust(8), str(val).rjust(4), sep=':')

# for num in range(1,31) :
#     print("은행 대기 번호 {0}번".format(str(num).zfill(3))) # 001, 002, 003 채움

#빈자리 두고 오른쪽 정렬, 10자리 공간 확보
print("{0: >10}".format(500))
#양수일때는 + 음수일때는 -
print("{0: >+10}".format(500))
print("{0: >-10}".format(-500))
#왼쪽 정렬 후 빈자리 _으로 채움
print("{0:_<+10}".format(500))
# 세자리마다 콤마 찍기
print("{0:,}".format(10000000))
# 세자리마다 콤마 찍고, 부호 붙이고 자릿수 확보, 빈칸 ^ 처리
print("{0:^<+30,}".format(100000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 두자리까지 출력
print("{0:.2f}".format(5/3))

# 쓰기 파일
# score_file = open("score.txt", 'w', encoding="utf8")
# print("수학 : 100", file=score_file)
# print("영어 : 80", file=score_file)
# score_file.close()

# append 파일
# score_file = open("score.txt", 'a', encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write('\n코딩 : 100')
# score_file.close

# 읽기 파일
# score_file = open("score.txt", 'r', encoding='utf8')
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", 'r', encoding='utf8')
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", 'r', encoding='utf8')
# while True :
#     line = score_file.readline()
#     if not line :
#         break
#     print(line)
# score_file.close()

# score_file = open("score.txt", 'r', encoding='utf8')
# line = score_file.readlines() # 리스트 형태로 저장
# print(line)
# score_file.close()

#pickle

# import pickle
# profile_pickle = open('profile_pickle', 'wb')
# profile = {'이름' : '성은진'}
# pickle.dump(profile, profile_pickle)
# profile_pickle.close()

# profile_pickle = open('profile_pickle', 'rb')
# profile = pickle.load(profile_pickle)
# print(profile)
# profile_pickle.close()

# with open('study.txt', 'w', encoding='utf8') as study_file :
#     study_file.write("파이썬 공부중")

# with open ('study.txt', 'r', encoding='utf8') as study_file :
#     print(study_file.read())

# 퀴즈
# for x in range(1, 51) :
#     with open (str(x)+'주차 보고서.txt', 'w', encoding='utf8') as report :
#         report.write('-'+str(x)+'주차 주간 보고 -\n')
#         report.write('이름 : \n')
#         report.write('업무 요약 :')
    

#퀴즈
class House:
    #매물 초기화
    def __init(self, location, house_type, deal_type, price, completion_year) :
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self) :
        print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

    

class Apt (House) :
    def __init__(self, location, house_type, deal_type, price, completion_year) :
        House.__init__(self, location, house_type, deal_type, price, completion_year)
        House.show_detail(self)


class Opi (House) :
    def __init__(self, location, house_type, deal_type, price, completion_year) :
        House.__init__(self, location, house_type, deal_type, price, completion_year)
        House.show_detail(self)


class vila (House) :
    def __init__(self, location, house_type, deal_type, price, completion_year) :
        House.__init__(self, location, house_type, deal_type, price, completion_year)
        House.show_detail(self)


Apt("강남", "아파트", "매매", "10억", "2010년")


