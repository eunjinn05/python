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