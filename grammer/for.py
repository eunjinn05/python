for waiting_no in [0,1,2,3,4,5] :
    print("대기 번호 : {0}".format(waiting_no))

for waiting_no in range(1, 6) :
    print("대기번호 : {0}".format(waiting_no))


#한줄 for문
student = ['emily', 'john', 'emma', 'jane']
student = [len(i) for i in student]
print(student)

student = ['emily', 'john', 'emma', 'jane']
student = [i.upper() for i in student]
print(student)