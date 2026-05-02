import tkinter as tk
from tkinter import messagebox

# 피자 가격 설정
pizza_menu = {
    "치즈 피자": 3000,
    "페퍼로니 피자": 3500,
    "불고기 피자": 4000,
    "하와이안 피자": 3800
}

# 총 금액 계산 함수
def calculate_total():
    total = 0
    order_list = []

    for pizza, var in check_vars.items():
        if var.get() == 1:
            try:
                qty = int(entry_vars[pizza].get())
                if qty < 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("입력 오류", f"{pizza} 수량을 올바르게 입력하세요.")
                return

            price = pizza_menu[pizza] * qty
            total += price
            order_list.append(f"{pizza} x {qty} = {price}원")

    if not order_list:
        messagebox.showwarning("주문 없음", "피자를 선택하세요!")
        return

    result_text.set("\n".join(order_list) + f"\n\n총 금액: {total}원")


# 메인 윈도우 생성
root = tk.Tk()
root.title("조각 피자 주문 프로그램")
root.geometry("350x400")

# 변수 저장용 딕셔너리
check_vars = {}
entry_vars = {}

tk.Label(root, text="🍕 피자 메뉴 선택", font=("Arial", 14)).pack(pady=10)

# 메뉴 생성
for pizza in pizza_menu:
    frame = tk.Frame(root)
    frame.pack(anchor="w", padx=20)

    check_vars[pizza] = tk.IntVar()
    entry_vars[pizza] = tk.StringVar(value="0")

    tk.Checkbutton(frame, text=f"{pizza} ({pizza_menu[pizza]}원)", 
                   variable=check_vars[pizza]).pack(side="left")

    tk.Entry(frame, width=5, textvariable=entry_vars[pizza]).pack(side="right")

# 계산 버튼
tk.Button(root, text="주문 계산", command=calculate_total).pack(pady=20)

# 결과 출력
result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, justify="left").pack()

# 실행
root.mainloop()