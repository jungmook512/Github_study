# 1. 파이썬에서 이터레이터(iterator)의 주요 특징은 무엇인가요? b
# a) 반복 가능한 객체를 생성한다.
# b) next() 메서드로 값을 순차적으로 반환한다.
# c) 리스트나 튜플만 이터레이터가 될 수 있다.
# d) 이터레이터는 재사용 가능하다.

# 2. 다음 코드의 실행 결과는 무엇인가요? b
# nums = [1, 2, 3]
# it = iter(nums)
# print(next(it))
# print(next(it))
# a) 1
# b) 1\n2
# c) 2
# d) 에러 발생

# 3. 다음 코드의 출력 결과는 무엇인가요? b
# def my_gen():
#     yield 1
#     yield 2
#     yield 3
# gen = my_gen()
# print(next(gen))
# print(next(gen))
# a) 1
# b) 1\n2
# c) 1\n3
# d) 에러 발생

# 4. 다음 중 제너레이터 표현식의 올바른 예는 무엇인가요? b
# a) [x * 2 for x in range(5)]
# b) (x * 2 for x in range(5))
# c) {x * 2 for x in range(5)}
# d) lambda x: x * 2 for x in range(5)

# 5. 다음 코드의 실행 결과는 무엇인가요? a
# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1
# gen = countdown(3)
# for x in gen:
#     print(x, end=" ")
# a) 3 2 1
# b) 1 2 3
# c) 에러 발생
# d) 3 3 3

# 6. 주어진 리스트를 이터레이터로 변환하고, 각 요소를 하나씩 출력하는 프로그램을 작성하세요.
# numbers = [1, 2, 3, 4, 5]


# iter_num = iter(numbers)

# for item in iter_num:
#     print(item)

# 7. 주어진 리스트에서 next() 함수를 사용하여 각 요소를 하나씩 출력하세요. StopIteration 예외를 처리하여 출력이 끝날 때까지 반복되도록 하세요.
fruits = ["apple", "banana", "cherry"]

iter_fruits = iter(fruits)

while True:
    try:
        print(next(iter_fruits))
    except StopIteration:
        break

# 8. 0부터 9까지의 숫자를 이터레이터로 순회하며, 각 숫자의 제곱을 출력하는 프로그램을 작성하세요.

i = (x * x for x in range(0,10))

for item in i:
    print(item)

# 9. 0부터 10까지의 숫자 중 짝수만 출력하는 프로그램을 작성하세요. 이때, 이터레이터를 사용해야 합니다.

i = (x for x in range(0,11) if x % 2 == 0)

for item in i:
    print(item)