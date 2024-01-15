#1
# n = int(input("정수 n을 입력하시오:"))
# for i in range(1, 100):
#     if n*i <= 100:
#         print(f"{n*i}")
#     else:
#         pass

num = int(input("정수 입력:"))
for i in range(101):
    if i % num == 0:  #배수 공식
        print(i)

# #2
# n = int(input("정수 n을 입력하시오:"))
# for i in range(1,10):
#     print(f"{n}*{i} = {n*i}")

