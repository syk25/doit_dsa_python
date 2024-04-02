d = [0] * 100


def fibo2(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = fibo2(n - 1) + fibo2(n - 2)
    print(n,'번째 함수 호출 합니다.')
    return d[n]

print(fibo2(99))