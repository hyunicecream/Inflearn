# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복은 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
#  -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
#  -- 축하합니다 --

# from random import *
# lst = [1,2,3,4,5]
# print(lst) # 원본 리스트
# shuffle(lst) # 리스트를 뒤섞기
# print(lst) # 섞은 후 리스트
# print(sample(lst, 1)) # 리스트 내에서 1개를 무작위로 뽑기(random)

from random import *

users = list(range(1, 21)) # 1부터 20까지 숫자를 생성
shuffle(users)
chicken = sample(users, 1)
del_chicken =  set(users) - set(chicken)
coffee = sample(del_chicken, 3)

print("--", "당첨자 발표", "--")
print("치킨 당첨자 : {0}".format(chicken))
print("커피 당첨자 : {0}".format(coffee))
print("--", "축하합니다", "--")
print("="*20)


print("나는 코딩의 풀이")
users = range(1, 21)
users = list(users)
print(users)
shuffle(users)
print(users)

winners = sample(users, 4)

print("--", "당첨자 발표", "--")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--", "축하합니다", "--")