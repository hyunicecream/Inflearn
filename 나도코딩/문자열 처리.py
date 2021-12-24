# <슬라이싱>
hyun = "90315-123315"
print("성별:", hyun[7])
print("성별:", hyun[0:3]) #0 ~3 직전까지
print("성별:", hyun[2:4])

# <문자열 처리 함수>
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index =python.index("n")
print(index)
index = python.index("n", index + 1) # 첫 번째 "n"말고 다음 "n"이 나오는 부분을 출력
print(index)
print(python.find("n"))  # find와 index의 차이 : find는 오류가 떠도 다음 출력을 실행, index는 터미널 종료
#print(python.index("Java"))
print("hi")
print(python.count("n"))


# <문자열 포맷>

# 방법 1
print('나는 %d살입니다.' % 20) # 정수
print("나는 %s를 좋아해요." % "파이썬") # 문자열
print("Apple 은 %c로 시작해요." % "A")  # 문자

print('나는 %s살입니다.' % 20) # 정수
print("나는 %s색과 %s색을 좋아해요." % ("파란", "노란"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "노란"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "노란"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "노란"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age =20, color='파란'))

# 방법 4 (v3.6 이상부터 사용가능)
age = 20
color = "초록"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# <탈출 문자>
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")
# \" \': 문장 내에서 따옴표
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")

# \\: 문장 내에서는 \
print("\\hyun@yuhyeonseung-ui-MacBookPro 혼자하는 파이썬 챌린지 % ")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스(한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

'''
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' + "!"로 구성
예) 생성된 비밀번호 : nav51!
'''

#url = "http://naver.com"
url = "http://google.com"
first_step = url.replace("http://", "")  # 규칙 1
print(first_step)
second_step = first_step[:first_step.index(".")] # first_step[0:5]
print(second_step)
last_step = second_step[:3] + str(len(second_step)) + str(second_step.count("e")) + "!"
print(last_step)


print('hello world')
print("hello world")








