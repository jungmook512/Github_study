

# def add_numbers(a, b):
#     result = a + b
#     print(result)

# add_numbers(2, 3)

# def message() :
#     print("A")
#     print("B")
# message()
# print("C")
# message()

# print("A")
# def message() :
#     print("B")
# print("C")
# message()

# num_list = [15, 20, 30, 40, 50]

# def calculate_average(num1_list):
#     total = 0
#     for i in num1_list:
#         total += i
#     avg = total / len(num1_list)
#     return avg

# average = calculate_average(num_list)
# print('평균 :', average)


def check_odd_even(a):
    if a % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

print(check_odd_even(4))   # 출력: Even
print(check_odd_even(7))   # 출력: Odd