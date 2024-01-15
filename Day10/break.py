#break: for, while의 반복을 끊는 역할
#continue: jump 같은 역할

for i in range(100):
    if i == 50:
        continue #50만 jump
    else:
        print(i)