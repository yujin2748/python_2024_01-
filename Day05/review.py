#1
a = float(input("밑변:"))
h = float(input("높이:"))
print(f"넓이 : {a * h * 0.5}, 둘레 : {3 * a}")

#2
t1 = input("원하는 운동 종류:")
t2 = input("원하는 운동 종류:")
t3 = input("원하는 운동 종류:")

print(f"운동 순서 : {t1} -> {t2} -> {t3}")


#3
movie = ['서울의 봄', '위시', '노량']
popcorn = ['팝콘', '치즈 팝콘', '카라멜 팝콘']
drink = ['콜라', '제로 콜라', '스프라이트']

a = int(input("영화 번호 고르시오!")) - 1
b = int(input("팝콘 번호 고르시오!")) - 1
c = int(input("음료 번호 고르시오!")) - 1

print(f"고르신 영화는 {movie[a]}이며 팝콘은 {popcorn[b]} 그리고 음료는 {drink[c]} 주문하셨습니다!")

