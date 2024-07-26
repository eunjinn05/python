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