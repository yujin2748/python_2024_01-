
# year = int(input("태어난 년도를 입력하시오:"))
# print(f"현재 만나이는 {2023 - year}입니다.")
#
# a = float(input("첫 번째 숫자를 입력하시오:"))
# b = float(input("두 번째 숫자를 입력하시오:"))
# c = float(input("세 번째 숫자를 입력하시오:"))
# print(f"평균은 {(a + b + c) / 3}입니다.")


#1
cel = float(input("섭씨 온도를 입력하시오:"))
fah = cel * 5.9 + 32
# 변수[실수]:.2f 둘째 자리 출력
print(f"화씨 온도는 {fah:.2f}입니다.")

#2
h = float(input("키를 입력하시오:"))
w = float(input("몸무게를 입력하시오:"))
bmi = w / (h ** 2)
print(f"bmi 수치는 {bmi:.2f} 입니다.")

#3
r = float(input("반지름을 입력하시오:"))
print(f"원의 넓이 : {r * r * 3.14}, 원의 둘레 : {2 * 3.14 * r}")


