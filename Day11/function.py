# 함수: 코드를 모아 놓은 묶음

# f(x) = x + 10
# input => 코드를 모아 놓은 묶음 => output

# 파이썬 내장 함수
# print() 함수
# input() 함수
# int() 함수
# enumerate() 함수

# 파이썬 커스터마이즈 함수
# def add(x, y):
#     result = x + y
#     return(result)
#
# a = add(5, 10)
# print(a)
#
# def minus(x, y):
#     result = x - y
#     return result
#
# b = minus(5, 10)
# print(b)
#
# def multiply(x, y):
#     result = x * y
#     return result
#
# c = multiply(5, 10)
# print(c)

# def odd_even(n):
#     if n % 2 ==0:
#         return "짝수입니다."
#     else:
#         return "홀수입니다."
#
# print(odd_even(6))

breads = ['소금빵', '보름달', '단팥빵', '앙버터', '마카롱']
prices = [2500, 1000, 2400, 4500, 3000]

def makeListDict(xList, yList, xKey = 'item', yKey = 'price'):  #기본값 설정
    return [{xKey: x, yKey: y} for x, y in zip(xList, yList)]

result = makeListDict(breads, prices)
print(result)