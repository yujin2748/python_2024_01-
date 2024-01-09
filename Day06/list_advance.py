# 리스트 연산자
# +: int + int (사칙 연산)
# +: str + str (문자 연결 연산)
# +: list + list (리스트 연결 연산)

coffee = ['아메리카노', '라떼', '바닐라 라떼']
cookie = ['화이트 쿠키', '녹차 쿠키', '오레오 쿠키']
menu = coffee + cookie

# * 연산자
# *: int * int (사칙 연산)
# *: str * int (str을 n번 반복)
# *: list * int (list를 n번 반복)
double_menu = menu * 2
print(double_menu)

# in 연산자: boolean 타입 변환
print('디카페인' in menu)

#[:] 슬라이싱 연산자
new_menu = menu[1:4]
print(new_menu)