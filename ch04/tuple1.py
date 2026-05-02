
# clovers = ('클로버1', '하트2', '클로버3')
# print(clovers[1])

# # clovers[1] = '클로버2'
# print(type(clovers))    #tuple

# # clovers[1] = '클러보2'

# my_tuple = ()       # 빈 튜플
# print(my_tuple)
# print(type(my_tuple))

# my_tuple2 = (1, -2, 3.14, True, "hi", [1,2])
# print(my_tuple2)

# my_tuple3 = 1, -2, 3.14, True, "hi", [1,2]
# print(my_tuple3)
# print(type(my_tuple3))

# # my_tuple3[3] = False      # TypeError

# my_int = (1)
# print(type(my_int))     # int
# my_int = (1,)
# print(type(my_int))     # tuple

# print('-----------------')
# # 형 변환 : list(), tuple()
# my_list3 = list(my_tuple3)
# print(my_list3)
# print(type(my_list3))       # list
# my_list3[3] = False
# print(my_list3)

# print('----------------')

t = ('a', 'b', 'c')

t1 = list(t)
print(t1)
t1[0] = 'A'
t = tuple(t1)
print(t)
print(type(t))