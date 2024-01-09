# key-value

# key: 중복 안됨, 숫자 or 문자 type 가능
# value: 중복 가능, any type
'''
zodiac = {
    1:'쥐',
    2:'소',
    3:'호랑이',
    4:'토끼',
    5:'용'
} #dict type

print(zodiac[4])
'''

mbti = {
    'e':'외향적',
    'i':'내향적',
    's':'감각적',
    'n':'직관적',
    'f':'감성적',
    't':'이성적',
    'j':'계획적',
    'p':'즉흥적',
}

print(mbti['e'])

personality = input("mbti를 입력하시오.:")
print(personality[0]) #e
print(f"당신은 {mbti[personality[0]]}이고, {mbti[personality[1]]}이고, {mbti[personality[2]]}이고, {mbti[personality[3]]}이시군요.")