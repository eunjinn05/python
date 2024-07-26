customer = '손님'
index = 5
while index >= 1 :
    print("{0}, 커피가 나왔습니다. {1}번 남았습니다.".format(customer, index))
    index -= 1
    
    if index == 0 :
        print('커피가 사라졌습니다.')

customer = '손님'
person = ''
while customer != person :
    print("{0}님, 커피가 준비되었습니다.".format(customer))
    person = input('이름이 어떻게되세요?')

    if person != customer :
        print('아직 커피가 나오지않았습니다. 기다려주세요')
    else :
        print('커피 나왔습니다')

absent = [3,5]
no_book = [7,9]
for student in range(1,20) :
    if student in absent :
        continue
    elif student in no_book :
        print("{0}번, 책 가져와".format(student))
        break
    else :
        print("{0}번, 책 읽어봐".format(student))