def ABCC () :
    return 'ABC'

print(ABCC())

def school_location (name, location) :
    print(name,'는 ',location,'에 있습니다.')

school_location("서울대", "관악구")
school_location(location="신촌", name="연세대")
school_location(name = "한양대", location = "왕십리")

def school_data (location, *name) :
    for school in name :
        print("{0}에 있는 학교는 {1}입니다".format(location, school))

print(school_data("신촌", '서강대', '연세대', '이화여대'))