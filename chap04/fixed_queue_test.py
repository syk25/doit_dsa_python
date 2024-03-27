from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum("Menu", ["인큐", "디큐", "피크", "검색", "덤프", "종료"])


def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f"({m.value}){m.name}" for m in Menu]

    while True:
        print(*s, sep=" ", end="")
        
        try:
            n = int(input(": "))
        except:
            print('번호를 잘못 입력했습니다. 다시 입력해주세요')
            n = 0
        if 1 <= n <= len(Menu):
            return Menu(n)


q = FixedQueue(64)

while True:
    print(f"현재 데이터 개수: {len(q)} / {q.capacity}")
    menu = select_menu()

    if menu == Menu.인큐:
        x = int(input("인큐할 데이터를 입력하세요: "))
        try:
            q.enqueue(x)
        except FixedQueue.Full:
            print("큐가 가득 찼습니다.")

    elif menu == Menu.디큐:
        try:
            x = q.dequeue()
            print(f"{x}를 디큐했습니다.")
        except FixedQueue.Empty:
            print("큐가 비어 있습니다.")

    elif menu == Menu.피크:
        try:
            x = q.peek()
            print(f"{x}를 피크했습니다.")
        except FixedQueue.Empty:
            print("큐가 비어 있습니다.")

    elif menu == Menu.검색:
        my_search = int(input("검색할 데이터를 입력하세요: "))
        if my_search in q:
            print(f"큐에 {my_search}가 {x}개가 있습니다.")
        else:
            print(f"큐에 {my_search}를 찾을 수 없습니다.")
    
    elif menu == Menu.덤프:
        q.dump()
    else:
        break

