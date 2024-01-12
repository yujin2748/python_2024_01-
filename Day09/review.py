#1
angle = int(input("각도를 입력하시오.:"))

if 0 < angle < 90:
    print("예각입니다.")
elif angle == 90:
    print("직각입니다.")
elif 90 < angle < 180:
    print("둔각입니다.")
elif angle == 180:
    print("평각입니다.")

#2
entrance = {
    'entSort': ['1. 일반 입장권', '2. 프리미엄 입장권', '3.VIP 입장권'],
    'price': [50000, 75000, 100000],
    'discount': ['1. 12세 미만 50% 할인', '65세 이상 30% 할인']
}

age = int(input("나이를 입력하시오.:"))
a = int(input(f"{entrance['entSort']}\n입장권을 선택하시오.:")) - 1

if age < 12:
    print(f"총 가격은 {entrance['price'][a] * 0.5}원 입니다.")
elif age > 65:
    print(f"총 가격은 {entrance['price'][a] * 0.7}원 입니다.")
else:
    print(f"총 가격은 {entrance['price'][a]}원 입니다.")

#3
import random

a = []
for i in range(6):
    a.append(random.randint(0, 10001))
a.sort()
print(a)