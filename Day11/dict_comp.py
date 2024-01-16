# normalPopcorn = {
#         'name':'일반 팝콘',
#         'price': 2500
# }

# coffee = ['아메리카노', '라떼', '바닐라']
# price = [2500, 3000, 3500]
#zipper
# zipped = zip(coffee, price)
# print(list(zipped))  # [('아메리카노', 2500), ('라떼', 3000), ('바닐라', 3500)]

# coffee = ['아메리카노', '라떼', '바닐라']
# price = [2500, 3000, 3500]
# caffeine = [120, 150, 50]
# result = [{'name': x, 'price': y, 'caffeine': z} for x, y, z in zip(coffee, price, caffeine)]
# print(result)

coffee = ['아메리카노', '라떼', '바닐라']
price = [2500, 3000, 3500]

k = {index: {'이름': coffee, '가격': price} for index, (coffee, price) in enumerate(zip(coffee, price))}
print(k)

# for index, item in enumerate(coffee):
#     print(f"{index}. {item}")

fruits = ['apple', 'mango', 'banana']
# 몇 번째인지 확인하고 싶으면 enumerate(열거한다)
for index, fruits in enumerate(fruits):
    print(f"{index}. {fruits}")