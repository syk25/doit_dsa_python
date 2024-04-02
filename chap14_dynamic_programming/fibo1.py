def fibo(n: int) -> int:
    if n == 2 or n == 1:
        return 1
    print(n,'번째 함수 호출 합니다.')
    return fibo(n - 1) + fibo(n - 2)


print(fibo(99))
