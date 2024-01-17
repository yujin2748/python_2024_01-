# comprehension
# for 문의 심화라 읽고 단축 버전

# 기본
# [i for i in range(10)] # 0 ~ 9
# [i for i in range(101)] # 0~ 100
# [i for i in "snow"] # 's', 'n', 'o', 'w'

# 필터링
# [i for i in range(10) if i % 2 == 0] # 짝수 모음

# 맵핑[변환/치환]
# ['😎' if i % 2 == 0 else '👀' for i in range(10)]

# dict
# coffee = ['아메리카노', '라떼', '힘들다커피']
# price = [2500, 3000, 5000]
# zip화
# 리스트 안에 dict
# [{'coffee': c, 'price': p} for c, p in zip(coffee,price)]
# dict 안에 dict
# {i:{'coffee': c, 'price': p} for i,(c,p) in enumerate(zip(coffee,price))}
#