
# 값 추가하기
# 리스트명.append(추가할 값)

listc = []
print(listc)
print(type(listc))

listc.append(300)
listc.append("파이썬")
print(listc)

listc.append(3.7)
print(listc)

listc.append(4<3)
print(listc)

# 값 제거하기
# 리스트명.remove(제거할값)

subject = ['국어', '수학', '영어', '국사']
print(subject)
subject.append('영어')
print(subject)
subject.append('영어')
print(subject)
subject.remove('영어')
print(subject)
subject.remove(subject[4])
print(subject)

clovers = ['클로버1', '클로버2', '클로버3']
print(clovers[1])
print(clovers)
del clovers[1]
print(clovers)

print(clovers[1])
del clovers[1]
print(clovers)

clovers.insert(0,'클로버5')
print(clovers)

clovers.extend(['zmffjqh8','클로버9'])
print(clovers)

