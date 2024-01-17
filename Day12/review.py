#1
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
a = [i for i in words if len(i) > 5 and i.count('a') > 0]
print(a)

#2
numbers = [30, 55, 20, 75, 40, 90, 10, 65]
b = [i for i in numbers if i > 50]
print(b)

#3
def plusOrMinus(a,b,flag):
    if flag:
        return a + b
    else:
        return a - b

print(plusOrMinus(34, 21, 0<3)

