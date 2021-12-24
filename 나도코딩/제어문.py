#### if 문 ####
# if 조건:
#     #실행 명령문
weather = "미세먼지"
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else: 
    print("준비물이 필요 없어요.")

weather = input("오늘 날씨는 어때요? ")
if weather == "비" or weather =="눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else: 
    print("준비물이 필요 없어요.")

temp = int(input("기온은 어때요?"))
if 30 <= temp:
    print("너무 더워요. 나가지마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10:
    print("외투를 챙기세요")
else: 
    print("너무 추워요. 나가지 마세요")

### for 문 #####
randrange()
for waiting_no in range(1, 6):
    print("대기번호 : {}".format(waiting_no))

starbucks = ["아이언맨", "토르", "헐크", "아이엠 그루트"]   
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

### while 문 ####
while (조건):
    customer = "토르"
    index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1} 번 남았어요".format(customer, index))
    index -= 1
    if index  == 0:
        print("커피는 폐기처분되었습니다.")

customer = "아이언맨"
index = 1
while True:
    print("{0}, 커피가 준비되었습니다. 호출 {1} 회".format(customer, index))
    index += 1

customer = "토르"
person = "Unknown"

while person != customer :
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")

#### continue 와 break ####
absent = [2, 5] # 결석
no_book =[7] # 책을 깜빡했음
for student in range(1, 10):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

#### 한줄로 끝내는 for 문 ####
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

'''
#### Quiz #####
당신은 Cocoa 서비스를 이용하는 택시 기사입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

출력문 예제
[0] 1번째 손님 (소요시간 : 15분)
[0] 2번째 손님 (소요시간 : 15분)
[0] 3번째 손님 (소요시간 : 15분)
...
[0] 50번째 손님 (소요시간 : 15분)
'''
# 총 탑승 승객 : 2분
from random import *
cnt = 0
for i in range(1, 51):
    time = randrange(5, 50)
    if 5 < time < 15: # 매칭성공
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: # 매칭이 실패한 경우
        print("[] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객 : {0} 분".format(cnt))        
print(int(cnt[0:3]))