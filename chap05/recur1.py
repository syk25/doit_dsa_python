def recur(n: int):
    """순수한 재귀함수 recur의 표현"""
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)


x = int(input("정수값을 입력하세요: "))

recur(x)
