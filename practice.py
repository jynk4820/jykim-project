from random import *
from math import *
print(5)
print(-10)
print(3.14)
print(1000)
print(3+5)
print(3*4)
print(3*(3+4))
print(2**3)  # 세제곱
print(5 % 3)  # 나머지구하기
print(5//3)  # 몫구하기
print(4 >= 7)
print(3 == 3)
print(3 == 4)
print(1 != 3)
print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))
print((3 > 0) or (3 < 2))
print((3 > 0) | (3 > 4))
print('풍선')
print("나비")
print("ㅋ"*9)
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)
number %= 5
print(number)

print(abs(-5))
print(pow(4, 2))
print(max(5, 12))
print(min(5, 12))
print(round(3.14))
print(round(4.99))

print(floor(4.99))
print(ceil(3.14))
print(sqrt(16))

print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)  # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 0.0 ~ 10.0 미만의 임의의 정수값 생성
print(int(random() * 10) + 1)  # 1.0 ~ 10.0 미만의 임의의 정수값 생성

print(int(random() * 45) + 1)  # 1.0 ~ 45.0 미만의 임의의 정수값 생성
print(int(random() * 45) + 1)  # 1.0 ~ 45.0 미만의 임의의 정수값 생성
print(int(random() * 45) + 1)  # 1.0 ~ 45.0 미만의 임의의 정수값 생성
print(int(random() * 45) + 1)  # 1.0 ~ 45.0 미만의 임의의 정수값 생성
print(int(random() * 45) + 1)  # 1.0 ~ 45.0 미만의 임의의 정수값 생성
print(int(random() * 45) + 1)  # 1.0 ~ 45.0 미만의 임의의 정수값 생성

print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성

print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성


sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이선은 쉬워요"
print(sentence2)
sentence3 = '''
나는 소년이고
파이선은 쉬워요
'''
print(sentence3)


jumin = "910112-1093311"

print("성별 = : " + jumin[7])
print("년도 = " + jumin[0:2])
print("월 = " + jumin[2:4])
print("일 = " + jumin[4:6])

print("생년월일 = " + jumin[:6])
print("뒤 7자리 " + jumin[7:])
print("뒤 7자리 = " + jumin[-7:])

python = "python is amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java"))
# print(python.index("Java")) 주석 풀면 오류 발생해서 밑에 코드들 실행안됨
print("hi")

print(python.count("n"))


print("나는 %d살입니다." % 20)
print("나는 %s을 좋아합니다." % "파이썬")
print("Apple은 %s 로 시작해요" % "A")
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아합니다." % ("파란" , "빨간"))

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란" , "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란" , "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란" , "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20 , color = "파란"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "파란" , age = 20))

age = 20
color = "파란"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

print("백문이 불여일견\n백견이 불여일타")
print('저는 "김지윤" 입니다.')
print("저는 \"김지윤\" 입니다.")
print("저는 \'김지윤\' 입니다.")

print("/Users/Jiyoon/Documents/pythonWorkSpace")
print("\\Users\\Jiyoon\\Documents\\pythonWorkSpace")

print("Red Apple\rpine")

print("Redd\bApple")

print("Red\tApple")

subway = [10, 20, 30]
print(subway)

subway = ["유재석" , "조세호" , "박명수"]
print(subway.index("조세호"))

subway.append("하하")
print(subway)

subway.insert(1 , "정형돈")
print(subway)

print(subway.pop())
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

#num_list.clear()
#print(num_list)

mix_list = ["조세호", 20, True]
print(mix_list)

num_list.extend(mix_list)
print(num_list)

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])

# print(cabinet.get(3))
# print(cabinet[5])
# print("hi")

print(cabinet.get(5))
print("hi")

print(cabinet.get(5, "사용가능"))
print("hi")

print(3 in cabinet)
print(5 in cabinet)


cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])

cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

del cabinet["A-3"]
print(cabinet)
 
print(cabinet.keys())

print(cabinet.values())

print(cabinet.items())

cabinet.clear()
print(cabinet)


menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
# menu.add("생선까스")

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)


my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

print(java & python)
print(java.intersection(python))

print(java | python)
print(java.union(python))

#집합은 순서없다

print(java - python)
print(java.difference(python))


python.add("김태호")
print(python)

java.remove("김태호")
print(java)


menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


