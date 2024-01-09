# 리스트 기능

#1 리스트의 길이 기능: len()
store = ['cu', 'gs', 'seven', 'ministop']
print(len(store))

#2 리스트 추가: append(무엇을)
store.append('emart24')
print(store)

#3 리스트 추가[몇 번째]: insert(몇 번째, 무엇을)
store.insert(1, 'familyMart')
print(store)

#4 리스트 제거: remove(무엇을)
store.remove('cu')
print(store)

#5 리스트 해당 아이템 위치 찾기: index(무엇을)
print(store.index('ministop'))

#6 리스트에 해당 아이템 몇 개 세기: count(무엇을)
print(store.count('emart24'))

#7 리스트를 추가: extend(리스트) +[같은 역할]
newStore = ['storyway', 'buytheway']
store.extend(newStore)
print(store)

#8 리스트 정렬: sort() / sort(reverse=true)
store.sort()
print(store)
store.sort(reverse=True) #역으로
print(store)