# 리스트
subway = [10, 20, 30]
print(subway)
subway = ['강아지', '고양이', '토끼']

print(subway.index('강아지'))
subway.append('호랑이')
print(subway)

subway.insert(1, '강아지')
print(subway)

print(subway.pop())
print(subway.count('강아지'))

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
mix_list = ['강아지', 30, True]

mix_list.extend(subway)
print(mix_list)