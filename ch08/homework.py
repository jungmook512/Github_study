
# x = 42
# y = 42

# print(id(x))
# print(id(y))
# print(id(x) == id(y))

# a = [3, 6, 7, 4, 9, 10, 13]


# def feven_lodd_swap(fa):
#     for i in  range(0, len(fa), 1):
#         if fa[i] % 2 ==0:
#             even_idx = i
#             break
#     for i in range(0, len(fa), 1):
#         if fa[i] % 2 ==1:
#             odd_idx = i
#     temp = fa[even_idx]
#     fa[even_idx] = fa[odd_idx]
#     fa[odd_idx] = temp
#     return fa

# print(feven_lodd_swap(a))

# def sumd(fa):
#     sum1 = 0
#     for i in fa:
#         sum1 += fa[i]
#     return sum1
# fb = {'a':10, 'b':20}

# print(sumd(fb))



class Phone:
    def __init__(self, number, color):
        self.number = number
        self.color = color

phone = Phone("010-1234-5678", "검정")
print(phone.number)
print(phone.color)

smartphone = Phone()