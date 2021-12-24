import theater_module 
theater_module.price(3) # 3명에서 영화 보러 갔을 때 가격
theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
theater_module.price_solider(5) # 5명의 군인이 영화보러 갔을 때

import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_solider(5)

from theater_module import *
price(3)
price_morning(4)
price_solider(5)

from theater_module import price, price_morning
price(5)
price_morning(6)
price_solider(7) # import에 안쓰면 못씀

from theater_module import price_solider as price
price(5)