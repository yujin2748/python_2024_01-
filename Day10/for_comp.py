#for_comp(심화/축약 버전)

# a = []
# for i in range(1001):
#     a.append(i)

# a = [i for i in range(1001)]
# b = [i for i in range(101)] #1 ~ 100
# c = [i for i in range(1, 501)] #1 ~ 500
# d = [i for i in "megastudy"]

# e = [i*2 for i in range(1, 101)]
# f = [i**2 for i in range(1, 11)]
# g = [i+5 for i in range(1,11)]

# for 컴프리헨션 조건문
# 1. if가 뒤에 있을 때는 filter 컷 역할
# [i for i in range(1, 101) if i % 5 == 0]
# fruits = ['apple', 'strawberry', 'mango', 'orange', 'melon']
# a = [i for i in fruits if i.count('a') > 0]
# b = [i for i in fruits if i.count('r') == 1]
# c = [i for i in fruits if len(i) >= 6]
# print(c)

# 2. if - else 있을 때는 map 변환 역할

# a = ['🍓' if i % 2 == 0 else i for i in range(1, 101)]

# n = int(input("정수 n을 입력하시오.:"))
# a = ['🥕' if i % n == 0 else i for i in range(1, 101)]
# print(a)
#
# fruits = ['apple', 'strawberry', 'mango', 'orange', 'melon']
# b = [i.upper() if len(i)<=5 else '🐇' for i in fruits]
# print(b)

# for 컴프리헨션 중첩 루프문

# h = [i*j for i in range(1, 3) for j in range(1,5)]
# g = [i+j for i in ["apple", 'banana'] for j in ["pie", "tanghuru"]]
# print(h)
# print(g)
