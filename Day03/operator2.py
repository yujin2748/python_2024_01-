# 산술 연산자[결과:숫자] +, -, *, /, //, %, **

# n = int(input("100이하의 정수를 입력하시오:"))
# print(f"10의 자리 : {n // 10}, 1의 자리 : {n % 10}")

# a = int(input("1000이하의 정수를 입력하시오:"))
# print(f"{(a//60)}분 {a%60}초")

n = int(input("10000~99999사이의 정수를 입력하시오:"))
print(f"100의 자리값은 {(n//100)%10}")



# 비교 연산자[결과:Bool]
# >, <, >=, <=, ==(같다), !=(다르다)
a = 3 > 1 # bool type
b = 3 == 1 # bool type [False]
c = 3 != 1 # bool type [True]

# 논리 연산자 [결과:bool]
# and: 피연산자가 모두 True이면 True
print(3 > 1 and 5 > 1) # True
# or: 피연산자가 하나라도 True이면 True
print(5 < 1 or 3 < 1 or 0 < 1) # True
# not: false -> true, true -> false
print(not(3 > 1)) # true -> false

# 할당 연산자
a = 1
a = 3
# a 얼마? 3
b = 1
# b = b + 3 # 3을 더해주기
b += 3 # 3을 더해주기
b -= 3 # 3을 빼주기
b *= 3 # 3을 곱하기
b /= 3 # 3으로 나눠주기
