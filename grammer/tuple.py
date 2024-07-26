#튜플 - 고정
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