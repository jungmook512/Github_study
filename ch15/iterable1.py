

a = [1,2,3]

# next(a)     # TypeError

# => list는 이터레이트가 아니다.
iter_a = iter(a)
print(type(iter_a))

# print(next(iter_a))
# print(next(iter_a))
# print(next(iter_a))
# print(next(iter_a))     #Stopiteration

for i in iter_a : 
    print(i)

    
for i in iter_a : 
    print(i)

print(next((iter_a)))