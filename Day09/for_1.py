# for x in 'icecream':
#     print(x)  # i c e c r e a m

# 1
# user = input("단어를 입력하시오.:")
# word = ''
# for x in user:
#     if x.isupper():
#         word += x.lower()
#     else:
#         word += x.upper()
# print(word)

#2
# user = input("단어를 입력하시오.:")
# word=''
# #apple
# for x in user:
#     if x == 'e' or x == 'a':
#         pass
#     else:
#         word += x
# print(word)

# if x in 'aeiou'  # 모음 빼기

# for x in [1, 2, 3, 4, 5]:
#     print(x ** 2)

# a = []
# for x in ['사과', '바나나', '파인애플']:
#     a.append(len(x))
# print(a)

# oddList = []
# evenSum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     if x % 2 == 1:
#         oddList.append(x)
#     else:
#         evenSum += x
# print(oddList)
# print(evenSum)

# import random
#
# list = []
# for i in range(100):
#     list.append(random.randint(0, 10001))
#
# newList=[]
#
# for j in range(100):
#     if list[j] % 2 == 0:
#         newList.append('🐇')
#     else:
#         newList.append('🥕')
#
# print(list)
# print(newList)

device = ['아이폰', '갤럭시', '맥북']
for x, y in enumerate(device):
    print(x, y)