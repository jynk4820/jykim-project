# 애완동물을 소개해 주세요

animal = "강아지"
name = "뽀롱이"
age = 11
hobby = "산책"
is_adult = age >= 3

'''이렇게 
하면 
여러문장이
주석처리 
됩니다 '''

print("우리집 " + animal + " 의 이름은 " + name + "에요")
# print(name + " 는 " + str(age) + " 살이고 " + hobby + "을 아주 좋아해요")
print(name, " 는 ", age, " 살이고 ", hobby, "을 아주 좋아해요")
# , 사용하면 빈칸이 하나 더 추가됨
print(name + " 는 어른일까요? " + str(is_adult))

# ctrl + / 전체 주석 처리 , 전체 주석 해제
