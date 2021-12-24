# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

# open_account()

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance 

def withdraw_nitght(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
# print(balance)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)


commission, balance = withdraw_nitght(balance, 500)
print("수수료는 {0} 원 이며, 잔액은 {1}".format(commission, balance))

def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어{2}".format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")


def profile(name, age=17, main_lang="파이썬"): 
    print("이름 : {0}\t나이 : {1}\t주 사용 언어{2}".format(name, age, main_lang))

profile("유재석")
profile("김태호")

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name='김태호')

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 :{0}\t나이 : {1}\t".format(name, age), end=" ") # end = 줄바꿈을 하지 않는다는 의미
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "python", "Jave", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")

def profile(name, age, *language):
    print("이름 :{0}\t나이 : {1}\t".format(name, age), end=" ") # end = 줄바꿈을 하지 않는다는 의미
    for lang in language:
        print(lang, end=" ")
    print()
profile("유재석", 20, "python", "Jave", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")

gun = 10
def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun
print("전체 총 : {0}".format(gun))
#checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

'''
 Quiz 표준 체중을 구하는 프로그램을 작성하시오
 표준 체중 : 각 개인의 키에 적당한 체중
 (성별에 따른 공식)
 남자 : 키(m) x 키(m) x 22
 여자 : 키(m) x 키(m) x 21
 
 조건1 : 표준 체중은 별도의 함수 내에서 게산
        함수명 : std_weight
        전달값 : 키(height), 성별(gender)
 조건2: 표준 체중은 소수점 둘재자리까지 표시

 (출력예제)
 키 175cm 남자의 표준 체중은 67.38kg 입니다.
'''
def std_weight(height, gender): # 키 m 단위 (실수), 성별 (string)
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)  # round -> 소수점 둘째 자리까지 표현
print(" 키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))


def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print(" 키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
