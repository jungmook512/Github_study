class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
         if not self.is_empty():
             return self.stack.pop()
         else:
             return -1

    def is_empty(self):
         return len(self.stack) == 0
    
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return -1
    
    def status_stack(self):
        return self.stack 
    

s = Stack()
s.push(6)
print(s.pop())

print("----------------------------")

def postfix_calc(expression):
    stack = []
    tokens = expression.split()  # 공백 기준으로 토큰 분리

    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token not in operators:
            stack.append(int(token))       # 숫자면 스택에 push

        else:
            b = stack.pop()                # 두 번째 피연산자
            a = stack.pop()                # 첫 번째 피연산자

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    print("❌ 0으로 나눌 수 없습니다.")
                    return None
                stack.append(a / b)

    return stack[0]  # 최종 결과


# 테스트
print(postfix_calc("3 4 +"))          # 3 + 4        = 7
print(postfix_calc("3 4 + 2 *"))      # (3 + 4) * 2  = 14
print(postfix_calc("5 1 2 + 4 * + 3 -"))  # 5+((1+2)*4)-3 = 14
print(postfix_calc("10 2 /"))         # 10 / 2       = 5.0

print("----------------------------")

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return -1
    
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return -1
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def status_queue(self):
        return self.queue
    
print("--------------------------------")

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return -1

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return -1

    def is_empty(self):
        return len(self.queue) == 0

    def status_queue(self):
        return self.queue


# ── 은행 창구 프로그램 ──────────────────────

bank = Queue()

# 1. 고객 도착 (Enqueue)
bank.enqueue('김철수')
bank.enqueue('이영희')
bank.enqueue('박민수')

# 2. 현재 대기열 확인
print(f"현재 대기열: {bank.status_queue()}")
print()

# 3. 순서대로 업무 처리 (Dequeue)
while not bank.is_empty():
    customer = bank.dequeue()
    print(f"업무 처리 중인 고객: {customer}")
    print(f"남은 대기 고객: {bank.status_queue()}")
    print()

print("-----------------------------------")

class Deque:
    def __init__(self):
        self.deque = []

    def push_front(self, x):
        self.deque.insert(0, x)     # 앞에 추가

    def push_back(self, x):
        self.deque.append(x)        # 뒤에 추가

    def pop_front(self):
        if not self.is_empty():
            return self.deque.pop(0)  # 앞에서 제거 후 반환
        return -1

    def pop_back(self):
        if not self.is_empty():
            return self.deque.pop()   # 뒤에서 제거 후 반환
        return -1

    def is_empty(self):
        return len(self.deque) == 0

    def status_deque(self):
        return self.deque