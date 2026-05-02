# generator.py

def simple_generator() :
    yield 'a'
    yield 'b'
    yield 'c'


g = simple_generator()
print(type(g))

print(next(g))
print(next(g))
print(next(g))
# print(next(g))

#제너레이터 이터레이터에 포함된다
# : 이터레이터가 더 큰 개념이고, 제너레이터는 그 구현 방법 중 하나 

print("------------------")
print(dir(g))

print('__iter__' in dir(g))
print('__next__' in dir(g))