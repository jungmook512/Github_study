

path = r"ch12\file1.txt"

f = open(path, "r", encoding="utf-8")

data = f.read()
print(type(data))
print(data)

f.close()