# print_func.py

na = 10
nb = 20.2
sa = "python"

print(na)
print(sa)
print(20.2)

result = print(na)
print(result)       # None

print(na, sa, 20.2)

result = na
print(result)       # 10

print("------------------")
print("na변수값", na)
print("nb변수값", nb)
print("sa변수값", sa)

print("-------------------")
nc = 30
nd = 40
print("nc=", nc, "nd=", nd)
nd = nc     #재할당
print("nc=", nc, "nd=", nd)