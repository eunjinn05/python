#if
weather = input("오늘 날씨가 어때요?")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
else :
    print("준비물이 필요없습니다")

temp = int(input("기온은 어때요?"))
if temp >= 30 :
    print("너무 더워요")
elif temp >= 20 and temp < 30 :
    print("좋아요")
else :
    print("추워요")