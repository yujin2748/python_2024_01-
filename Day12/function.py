# def name(x="버터", y ="빵"):
#     로직 작성
#     돌려 주는 값이 있으면 return

movie = ['1. 액션 영화', '2. 로맨틱 코미디', '3. 다큐멘터리']
moviePrice = [12000, 10000, 11000]
popcorn = ['1. 팝콘 세트', '2. 스낵 콤보', '3. 건강 팩']
popcornPrice = [6000, 8000, 7000]
seat = ['1. 일반 좌석', '2. 프리미엄 좌석', '3. VIP 좌석']
seatPrice = [0, 5000, 10000]

zipMovie = list(zip(movie, moviePrice))
zipPopcorn = list(zip(popcorn, popcornPrice))
zipSeat = list(zip(seat, seatPrice))

total = {
    '영화': zipMovie,
    '팝콘': zipPopcorn,
    '좌석': zipSeat
}

print(total['영화'])

a = int(input("영화 종류를 선택하시오.::")) - 1
b = int(input("스낵 패키지를 선택하시오.:")) - 1
c = int(input("좌석을 선택하시오.:")) - 1
age = int(input("나이를 입력하시오.:"))
totalPrice = moviePrice[a] + popcornPrice[b] + seatPrice[c]

def discount(totalPrice):
    if age < 18:
        totalPrice *= 0.8
        return totalPrice
    elif age >= 65:
        totalPrice *= 0.85
        return totalPrice
    else:
        return totalPrice

print(totalPrice)
print(f"총 가격은 {discount(totalPrice)}입니다.")